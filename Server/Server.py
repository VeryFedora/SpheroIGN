import socket
import threading
import queue
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5005))

# Each connected device will be represented as an instance of this class.
class ConnectedDevice:
    connectedDevices = []
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.id = len(ConnectedDevice.connectedDevices) + 1  # Simple ID assignment based on current count)
        ConnectedDevice.connectedDevices.append(self)

        sock.send(f"ACK_JOIN:{self.id}".encode('utf-8'), (self.ip_address, self.port))

    def __str__(self):
        return f"ConnectedDevice(ip_address={self.ip_address}, port={self.port})"

    
inbox = queue.Queue();

def PassiveReceiver():
    global sock, inbox
    while True:
        data, addr = sock.recvfrom(1024)
        # Store data with the exact float time of arrival
        inbox.put(
        {
            "time": time.time(), 
            "msg": data.decode('utf-8', 'ignore'),
            "sender": addr
        })

receiver_thread = threading.Thread(target=PassiveReceiver)
receiver_thread.start()

CollidedObjects = []

while 1:
    if not inbox.empty():
        msg = inbox.get()
        print(f"Received message from {msg['sender']}: {msg['msg']} at time {msg['time']}")

        if msg['msg'] == "JOIN":
            print(f"Device {msg['sender']} has joined the network.")
            ConnectedDevice(msg['sender'][0], msg['sender'][1])

        elif msg['msg'] == "LEAVE":
            print(f"Device {msg['sender']} has left the network.")
            for device in ConnectedDevice.connectedDevices:
                if device.ip_address == msg['sender'][0] and device.port == msg['sender'][1]:
                    ConnectedDevice.connectedDevices[device.id] = None  # Mark as None instead of removing to keep IDs consistent]
                    break

        elif msg['msg'] == "COLLISION":
            CollidedObjects.append(
                {
                    "time": msg['time'],
                    "sender": msg['sender']
                }
            )
