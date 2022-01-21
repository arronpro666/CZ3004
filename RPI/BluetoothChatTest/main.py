import bluetooth
import threading

def wait_for_client(socket, host, port):

    print("Waiting for connection...")

    socket.bind((host, port))
    socket.listen(1)

    client_sock, client_address = socket.accept()
    print(client_address)
    client_name = bluetooth.lookup_name(client_address[0])

    print(f"Connected to device {client_name} ({client_address})")

    return client_sock, client_address, client_name

def thread_receive(socket, client_name):
    while True:
        data = socket.recv(1024)

        if data:
            str = data.decode("utf-8")
            print(f"{client_name}: {str}")

def thread_send(socket):
    while True:
        user_input = input()

        if user_input is not None:
            socket.send(user_input)

def main():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_host = ""
    server_port = 1

    client_sock, client_address, client_name = wait_for_client(server_sock, server_host, server_port)
    
    t_recv = threading.Thread(target=thread_receive, args=(client_sock, client_name))
    t_send = threading.Thread(target=thread_send, args=(client_sock,))

    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()