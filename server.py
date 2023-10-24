import socket


def receive_message(client_socket):
    message = b""
    while True:
        data = client_socket.recv(1)
        if data == b'\n':
            break
        message += data
    return message


def send_message(client_socket, message):
    client_socket.send(message + b'\n')


def start_server():
    server_address = ('localhost', 12345)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Waiting for connections...")

    try:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        for i in range(1, 101):
            message = receive_message(client_socket)
            if not message:
                break  # No more data received, exit the loop

            print(f"Received from client: {message.decode()}")

            # Process the message and create a response
            response = f"Response from server to message {message.decode()}".encode()
            send_message(client_socket, response)

    except KeyboardInterrupt:
        print("Server has been interrupted.")
    finally:
        client_socket.close()
        server_socket.close()


if __name__ == "__main__":
    start_server()
