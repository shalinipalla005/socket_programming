import socket

def main():
    host = socket.gethostbyname(socket.gethostname())
    port = 12345        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        while True:
            expression = input("Enter a mathematical expression (or type 'exit' to quit): ")
            if expression.strip().lower() == "exit":
                print("Closing connection to server.")
                client_socket.send(expression.encode())
                break
            client_socket.send(expression.encode())
            result = client_socket.recv(1024).decode()
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
