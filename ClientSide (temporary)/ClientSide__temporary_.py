import socket
import threading
import queue
import time
import SYSLIB
# Actual socket used to send messages through. Sock is a fun name so i'm using it
sock : socket.socket = None;
# our inbox carries messages.
inbox : queue.Queue = None;


def receiverThread():
    global sock, inbox
    while :
        data, addr = sock.recvfrom(1024)
        # Store data with the exact float time of arrival
        inbox.put(
        {
            "time": time.time(), 
            "msg": data.decode('utf-8', 'ignore'),
            "sender": addr
        })


def initClient():
    # We are using UDP to minimize latency, but this means we have to handle packet loss. AF_INET means we are using IPv4, and SOCK_DGRAM means UDP.
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM means udp, why is the name DRGAM ;-;
    global inbox
    inbox = queue.Queue()
    # Start the receiver thread to listen for incoming messages
    thread = threading.Thread(target=receiverThread, daemon=True).start()
    threading.


