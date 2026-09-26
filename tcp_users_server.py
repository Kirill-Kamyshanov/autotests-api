import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен и ждёт подключений")

    all_messages = []

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Пользователь с адресом: {client_address} подключился к серверу')

        data = client_socket.recv(1024).decode()
        all_messages.append(data)
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        client_socket.send('\n'.join(all_messages).encode())


if __name__ == '__main__':
    server()
