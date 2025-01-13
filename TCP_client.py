import socket
host = socket.gethostbyname(socket.gethostname())
port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_client():
    
    try:
        client_socket.connect((host, port))
        print("Connected to the server.")
        message = "Hello, Server!"
        print(f"Sent to server: {message}")
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Received from server: {response}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        

if __name__ == "__main__":
    start_client()
    client_socket.close()
