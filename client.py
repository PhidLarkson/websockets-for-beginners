# import socket module
import socket
import time
from config import *

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
print(f'[CONNECTING TO {SERVER}]')
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)   # Get the length of the message
    send_length = str(message_length).encode(FORMAT)    # Encode the length of the message
    send_length += b' ' * (HEADER - len(send_length))   # Add padding to the length of the message: 64 bytes
    client.send(send_length)                   # Send the length of the message
    client.send(message)               # Send the message
    
    # Receive a response from the server
    print("Response: ", client.recv(HEADER).decode(FORMAT))

# Receive messages from the server
try: 
    while True:
        print(f'Type "{BREAK}" to quit')
        message = input('Enter message: ')
        if message == '':
            print('Message cannot be empty')
            continue
        if message == BREAK:
            print(f'[DISCONNECTING FROM {SERVER}]')
            send(message)
            break
        send(message)
except:
    print('An error occurred')
