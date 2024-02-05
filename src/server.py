import socket
import AppChatAI
listing_soket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listing_soket.bind(("127.0.0.1",5000))
listing_soket.listen()

while True:
    socket_for_communication,addr=listing_soket.accept()
    print("connect",addr)
    data = socket_for_communication.recv(1024)
    if data:
        print("data from client:",data)

    else:
        print("Error, while receiving data from socket")

socket_for_communication.close()