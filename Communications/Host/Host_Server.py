import socket
import MessageManager
import threading
import UserManager
import re
#V2 Route All custom Modules through Import Server_Interface 

def main():
    host = '192.168.56.1'  # Replace with your server's public IP address or hostname
    port = 5550  # Choose a port number
    MessageManager.onStart(99)
    print(MessageManager.bufferIndex)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    while True:
        print(f"Server listening on {host}:{port}")
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        thread = threading.Thread(target=run_server, args=(client_address, client_socket, server_socket))
        thread.start()
    
def run_server(client_address, client_socket, server_socket):
    addrstr = client_address[0]
    UserManager.logData(addrstr)
    try:
        client_socket.send(f'19 {UserManager.requestUser(addrstr)}'.encode())
        print(f'Awaiting Message from: {client_address}\n')
        
        while True:
            try:
                MessageManager.clearBuffer(addrstr, client_socket)
            except:
                pass
            data = client_socket.recv(1024)
            message = data.decode()
            print(f"Received from client: {message}")
            MessageManager.theMethod(addrstr,message)
                       
    except Exception as e:
        print(f'Error: {e}')
        UserManager.delogData(addrstr)
        client_socket.close()
        print("Server Disconnected")
    
def close_Client(client_socket, thread):
    print("4")
    thread.join

if __name__ == "__main__":
    main()