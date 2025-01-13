import socket
import threading

clients = {}
lock = threading.Lock()

def broadcast(message, sender_client=None):
    with lock:
        for client, username in clients.items():
            if client != sender_client:
                try:
                    client.send(message.encode())
                except:
                    remove_client(client)

def handle_client(client_socket):
    try:
        username = client_socket.recv(1024).decode()
        with lock:
            clients[client_socket] = username
        broadcast(f"{username} has joined the chat!")
        client_socket.send(f"Currently active users: {', '.join(clients.values())}".encode())
        print(f"{username} connected.")

        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == "exit":
                break
            broadcast(f"{username}: {message}", sender_client=client_socket)
    except:
        pass
    finally:
        remove_client(client_socket, notify=True)

def remove_client(client_socket, notify=False):
    with lock:
        username = clients.pop(client_socket, None)
    if username and notify:
        broadcast(f"{username} has left the chat.")
        print(f"{username} disconnected.")
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 12354))
    server_socket.listen(5)

    ip = socket.gethostbyname(socket.gethostname())
    print(f"Chat server running on {ip}:12354...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
