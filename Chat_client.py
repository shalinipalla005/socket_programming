import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("Disconnected from server.")
            break

def start_client():
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 12354

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print("Connected to the chat server.")

    username = input("Enter your username: ")
    client_socket.send(username.encode())
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input()
        if message.lower() == "exit":
            client_socket.send("exit".encode())
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
