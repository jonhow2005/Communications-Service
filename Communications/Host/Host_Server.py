import socket

def run_server():
    host = '192.168.56.1'  # Replace with your server's public IP address or hostname
    port = 5550  # Choose a port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                if socket.error:
                    break
                message = data.decode()
                print(f"Received from client: {message}")

                # Process data and send a response
                response = "Message received!"
                client_socket.send(response.encode())
            if socket.error:
                break
    except Exception as e:
        print(f'Error: {e}')
    finally:
        client_socket.close()
        print("Client Disconnected")

run_server()       
        
def close_Server(client_socket):
    
    client_socket.close()

