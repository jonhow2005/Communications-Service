import threading
import Server_Controller
import Client_Server

# Function to start the server
def start_server():
    Server_Controller.create_server()

# Function to start the client
def start_client():
    Client_Server.clntfunc()

# Start the client and server in separate threads
def main():
    # Start client in a separate thread
    client_thread = threading.Thread(target=start_client)
    client_thread.start()

    # Start server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Wait for threads to complete (if necessary)
    client_thread.join()
    server_thread.join()

if __name__ == "__main__":
    main()