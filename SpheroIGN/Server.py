import socket
import threading
import queue
import time
import SYSLIB
# a lot of this code is recycled from the client, it is just nice to have this on another thread to prevent ambiguity.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 0.0.0.0 means to let it listen for any interface for any device. i used 5005 because i felt like it and because its over 1024
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

# literally just a list of stuff we've collected.
inbox = queue.Queue();

def PassiveReceiver():
    global sock, inbox
    while True:
        data, addr = sock.recvfrom(1024)
        # Store data with the exact float time of arrival
        inbox.put(
        {   # I miss "struct" from C :(
            "time": time.time(), 
            "msg": data.decode('utf-8', 'ignore'),
            "sender": addr
        })

def start():
    receiver_thread = threading.Thread(target=PassiveReceiver)
    receiver_thread.start()

    CollidedObjects = []

    while SYSLIB.running.get():
        if not inbox.empty():
            msg = inbox.get()
            print(f"Received message from {msg['sender']}: {msg['msg']} at time {msg['time']}")

            if msg['msg'] == "JOIN":
                print(f"Device {msg['sender']} has joined the network.")
                sock.send(f"ACK_JOIN".encode('utf-8'), (msg['sender'][0], msg['sender'][1]))
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
    for device in ConnectedDevice.connectedDevices:
        if device != None:
            sock.send(f"SERVER_SHUTDOWN".encode('utf-8'), (device.ip_address, device.port))
    sock.detach();
    sock.shutdown();
