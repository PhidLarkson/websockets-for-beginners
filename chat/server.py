# import relevant libraries
import socket
import threading
from config.config import *
import blessings
import asyncio

#  Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

history = []

# ...
def handle_client(conn, addr):
    print(f'[NEW CONNECTION] user:{threading.active_count() - 1} connected.')   # Display the address of the client
    
    #chat id
    # client_name = addr_cv(PORT)
    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)      # Receive the message
        if msg:
            msg_length = len(msg)          # Get the length of the message
            # msg = int(msg)
            msg = conn.recv(msg_length).decode(FORMAT) 
            #add to history
            history.append(msg)  
            print(f'@{1} | {addr} {msg} \n{msg_length} bytes received\n')  # Display the message
                 
            if msg == BREAK:
                connected = False             # Break the connection   
        
        async def get_input():
            return input('Say something: ')

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        say_something = loop.run_until_complete(get_input())
        conn.send(say_something.encode())  # Send a response
    conn.close()
    
def start():
    server.listen()

    while True:
        conn, addr = server.accept()            # Accept the connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Create a thread
        thread.start()                        # Start the thread
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')    # Display the number of active connections

try:
    server.bind(ADDR)       # Bind the server to the address
    print(f'[LISTENING] Server is listening on {SERVER}')
    start() # Start the server  

except Exception:
        print("\nServer is shutting down...")
        server.close()
        print("Server has been shut down")
        exit()