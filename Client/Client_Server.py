import socket
import Server_Interface

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

def clntfunc():
    host = '0.0.0.0'  # Replace with the server's public IP address or hostname
    port = 5550
    global client_socket
    try:
        client_socket.connect((host, port))  # Connect to the external server
        print(f"Connected to server at {host}:{port}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response = data.decode()
            print(f"Received from server: {response}")
            Server_Interface.receiveCommand(response)
            print("Command Excecuted")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Disconnected from Server.")

    
    
def msgfunc(message):
    global client_socket
    print("sending " + message)
    client_socket.send(message.encode())

def close_client(message):
    global client_socket
    client_socket.send(message.encode())

