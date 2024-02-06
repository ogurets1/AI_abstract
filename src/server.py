import socket
import serverGUI



def create_socket():
    listing_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listing_socket.bind(("127.0.0.1", 9000))
    listing_socket.listen()
    return listing_socket


def accept_connection(listing_socket):
    socket_for_communication, addr = listing_socket.accept()
    print("Connected to", addr)
    return socket_for_communication


def receive_data(socket_for_communication):
    data = socket_for_communication.recv(1024)
    if data:
        print("Data from client:", data)
        serverGUI.log("Data from client:", data)
    else:
        print("Error while receiving data from socket")
    socket_for_communication.close()


def main():
    listing_socket = create_socket()

    while True:
        socket_for_communication = accept_connection(listing_socket)
        receive_data(socket_for_communication)


