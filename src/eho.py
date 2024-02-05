import socket
import threading
HOST = '127.0.0.1'    # all available interfaces
PORT = 5005  # any port > 1023

main_socket:socket.socket =None
stop_main_thread = False

def on_client_connected(conn: socket.socket, addr):
    print('Client connected: ', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
            conn.sendall(data)
    conn.close();
    print('Client disconnected: ', addr)

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)  # 10 means the number of accepted connections
    global main_socket
    global stop_main_thread
    main_socket = s
    print(f'Server started on port {PORT}, waiting for connections... (Press ENTER key to stop)')
    while True and not stop_main_thread:
        try:
            conn, addr = s.accept()  # waits for a new connection

            threading.Thread(target=on_client_connected, args=(conn, addr)).start()
        except:
            pass
    print('Server stopped.')
def stop_server():
    global stop_main_thread
    stop_main_thread = True
    # makes a dummy connection just to unlock accept method and trigger the gracefully stop    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((HOST, PORT))

main_thread = threading.Thread(target=start_server)
main_thread.start()
while True:
    user_input = input()
    if not user_input:  # i.e. enter key pressed
        break
print('Stopping server... ')
stop_server()
main_thread.join()
main_socket.close()