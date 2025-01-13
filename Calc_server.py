import socket

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    host = socket.gethostbyname(socket.gethostname())
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server is listening on port {port}...")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connection established with {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data or data.strip().lower() == "exit":
                    print("Closing connection to client.")
                    break
                print(f"Received expression: {data}")
                result = evaluate_expression(data)
                conn.send(result.encode())

if __name__ == "__main__":
    main()
