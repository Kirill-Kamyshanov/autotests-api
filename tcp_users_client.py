import socket


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = "127.0.0.1", 12345
    client_socket.connect(server_address)

    client_socket.send("Привет, сервер!".encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()


if __name__ == '__main__':
    client()
