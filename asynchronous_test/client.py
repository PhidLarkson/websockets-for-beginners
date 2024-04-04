import asyncio
import websockets
from config import *

async def send(websocket, msg):
    message = msg.encode(FORMAT)
    message_length = len(message)   # Get the length of the message
    send_length = str(message_length).encode(FORMAT)    # Encode the length of the message
    send_length += b' ' * (HEADER - len(send_length))   # Add padding to the length of the message: 64 bytes
    await websocket.send(send_length)                   # Send the length of the message
    await websocket.send(message)               # Send the message
    
    # Receive a response from the server
    response = await websocket.recv()
    print("Response: ", response.decode(FORMAT))

async def main():
    uri = f"ws://{SERVER}:{PORT}"
    async with websockets.connect(uri) as websocket:
        try: 
            while True:
                print(f'Type "{BREAK}" to quit')
                message = input('Enter message: ')
                if message == '':
                    print('Message cannot be empty')
                    continue
                if message == BREAK:
                    print(f'[DISCONNECTING FROM {SERVER}]')
                    await send(websocket, message)
                    break
                await send(websocket, message)
        except:
            print('An error occurred')

asyncio.run(main())
