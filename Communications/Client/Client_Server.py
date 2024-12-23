import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
def clntfunc():
    host = '192.168.56.1'  # Replace with the server's public IP address or hostname
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

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Disconnected from Server.")

    
    
def msgfunc(message):
    client_socket.send(message.encode())

def close_client(message):
    client_socket.send(message.encode())
