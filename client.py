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


def start_client():
    server_address = ('localhost', 12345)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(server_address)
        print("Connected to the server")

        for i in range(1, 101):
            message = f"Message {i} from the client".encode()
            send_message(client_socket, message)

            response = receive_message(client_socket)
            print(f"Received from server: {response.decode()}")

    except KeyboardInterrupt:
        print("Client has been interrupted.")
    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()
