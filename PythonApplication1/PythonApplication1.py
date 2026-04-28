import socket
import sys

# Force the terminal to show text immediately
print("1. Script has started...")

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Using 5005 to avoid port 1024 permission issues
    server_address = ('127.0.0.1', 5005)
    message = "hello"

    print(f"2. Attempting to send to {server_address}...")
    sock.sendto(message.encode(), server_address)
    
    print("3. Message sent successfully!")

except Exception as e:
    print(f"!!! ERROR: {e}")

finally:
    sock.close()
    print("4. Socket closed. Process finished.")

# Keeps the window open so it doesn't disappear
input("\nPress Enter to close this window...")