import socket
import asyncio
import websockets
from websockets.asyncio.server import serve
import Server_Interface
sendbool = False
globalmessage = ''
#V2 update: Clean file, integreate useful  unused code 
#Not used
def unused_server_method():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local hostname
    hostname = socket.gethostname()

    # Define the port number
    port = 5000

    # Bind the socket to a specific address and port
    server_socket.bind((hostname, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print(f"Server listening on {hostname}:{port}")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Handle the client request
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()}")
            client_socket.send(b"Hello from server")

  #       Close the client socket
        client_socket.close()
# Run the server
async def echo(websocket):
    global sendbool
    global globalmessage
    if sendbool == True:
        await websocket.send(globalmessage)
        sendbool = False
    async for message in websocket:
        print(f"Received message from frontend: {message}")
        message = Server_Interface.receiveCommand(message)
        print("Command Excecuted")
        print("sending to frontend", message)
        if message != None:
            await websocket.send(message) 
        
async def main_Asyncio():
    async with serve(echo, "localhost", 5000) as server:
        await server.serve_forever()

#create server
def create_server():
        asyncio.run(main_Asyncio())

#All Below Are Currently Unsused                 
async def event_handler(event):
    print("Event triggered!")

async def mainEvent():
    event = asyncio.Event()

    # Create a task to listen for the event
    listener_task = asyncio.create_task(event_handler(event))

    # Do some other work
    await asyncio.sleep(2)
    # Trigger the event
    event.set()

    # Wait for the listener to finish
    await listener_task

async def receive_message():
    queue = asyncio.Queue()
    message = await queue.get()
    print(f"Received message: {message}")
       
async def waitformessage_function():
    print("waitfor2")
    queue = asyncio.Queue()
    while True:
        print("waiting")
        instruction = await queue.get()
        #if str(instruction) == " Get IP ":
            #Ip_Finder.Getip()
        
def waitformessage():
    print("waitformessage")
    asyncio.run(waitformessage_function())
    
def waitformessage_debug():
    asyncio.run(receive_message())
    
async def messageGet(queue):
    queue = asyncio.Queue()
    asyncio.create_task(waitformessage_function(queue))
    

