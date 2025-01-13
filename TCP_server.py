import socket
host = socket.gethostbyname(socket.gethostname())  
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    server_socket.bind((host, port))
    print(f"Server is listening on {host}:{port}...")
    server_socket.listen(1) 
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        try:
            message = client_socket.recv(1024).decode()
            print(f"Received from client: {message}")
            response = f"Server says: {message}"
            client_socket.send(response.encode())
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            print("Connection closed.")
            client_socket.close()

if __name__ == "__main__":
    start_server()
