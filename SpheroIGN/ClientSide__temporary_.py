import socket
import threading
import queue
import time
import SYSLIB
import Server
# Actual socket used to send messages through. Sock is a fun name so i'm using it
sock : socket.socket = None;
# our inbox carries messages.
inbox : queue.Queue = None;
# 255.255.255 is the broadcast address, meaning that if we send to it, all devices on the network will receive it.
# i assure you thats standard and that on join_ack the address will be replaced.
server_address = ('255.255.255.255', 5005)
def receiverThread():
    global sock, inbox
    while SYSLIB.running.get():
        data, addr = sock.recvfrom(1024)
        # Store data with the exact float time of arrival
        inbox.put(
        {
            "time": time.time(), 
            "msg": data.decode('utf-8', 'ignore'),
            "sender": addr
        })
    print("thread closed.")
    sock.detach();
    sock.shutdown();


def getMessages():
    global inbox
    global server_address
    while not inbox.empty():
        message = inbox.get()
        if message["msg"] == "JOIN_ACK":
            server_address = message["sender"]
        # Note: Make it so that the server nominates a new one to take its place.
        if message["msg"] == "SERVER_SHUTDOWN":
            server_address;
    
receiver_thread = None;
def initClient():
    global receiver_thread; 
    # We are using UDP to minimize latency, but this means we have to handle packet loss. AF_INET means we are using IPv4, and SOCK_DGRAM means UDP.
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM means udp, why is the name DRGAM ;-;
    global inbox
    inbox = queue.Queue() 
    # Start the receiver thread to listen for incoming messages
    receiver_thread = threading.Thread(target=receiverThread, daemon=True).start()
    # The loop is simply so the server host can still play.
    for i in range(2): 
        sock.send("JOIN".encode(), server_address)
        time.sleep(1) # wait a second for the server to respond with the join ack, which will set the server address to the correct one. 
        # REPLACE THE SLEEP FUNCTION LATER! THAT IS NOT RELIABLE! (but neither is UDP so like idk man)
        if(server_address[0] != '255.255.255.255'):
            print(f"Successfully joined the network. Server address: {server_address}")
            break;
        else:
            threading.Thread(Server.start()) # if we didnt get a response, that means that there is no server so we host on ours. 



