import asyncio
from config import *
import blessings

# import relevant libraries

history = []

async def handle_client(reader, writer):
    print(f'[NEW CONNECTION] user:{len(asyncio.all_tasks()) - 1} connected.')   # Display the address of the client
    addr = writer.get_extra_info('peername')

    connected = True
    while connected:
        data = await reader.read(100)  # Receive the message
        msg = data.decode(FORMAT)
        if msg:
            msg_length = len(msg)          # Get the length of the message
            #add to history
            history.append(msg)  
            print(f'@{1} | {addr} {msg} \n{msg_length} bytes received\n')  # Display the message
                 
            if msg == BREAK:
                connected = False             # Break the connection   

        say_something = input('Say something: ')
        writer.write(say_something.encode())  # Send a response
        await writer.drain()

    print("Closing the connection")
    writer.close()

async def start():
    server = await asyncio.start_server(
        handle_client, SERVER, PORT)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

try:
    print(f'[LISTENING] Server is listening on {SERVER}')
    asyncio.run(start()) # Start the server  

except Exception:
    print("\nServer is shutting down...")
    print("Server has been shut down")
    exit()
