#!/usr/bin/env python
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Server: {message}")

        except ConnectionResetError:
            break

    print("Server connection closed.")
    client_socket.close()

def send_message(client_socket):
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

        # I-check kung ang mensahe ay "/quit" upang i-terminate ang loop
        if message == "/quit":
            break

    client_socket.close()

def main():
    host = '192.168.76.93'  # IP address ng server
    port = 5000  # Port number ng server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the server.")

    # Gumawa ng thread para sa pagtanggap ng mga mensahe mula sa server
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    # Gumawa ng thread para sa pagpapadala ng mga mensahe
    threading.Thread(target=send_message, args=(client_socket,)).start()

if __name__ == "__main__":
    main()

