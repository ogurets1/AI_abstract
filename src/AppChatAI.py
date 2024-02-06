import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
import socket

class ChatApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chat Application')
        # Создание поля для вывода чата
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        # Создание поля для ввода сообщения
        self.message_input = QLineEdit()
        # Создание кнопки для отправки сообщения
        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_message)
        # Размещение виджетов на форме
        layout = QVBoxLayout()
        layout.addWidget(self.chat_display)
        message_layout = QHBoxLayout()
        message_layout.addWidget(self.message_input)
        message_layout.addWidget(self.send_button)
        layout.addLayout(message_layout)
        self.setLayout(layout)
    def send_message(self):
        send_data = self.message_input.text()
        self.chat_display.append('You: ' + send_data)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 9000))
        client_socket.sendall(bytes(send_data, "utf-8"))
        self.message_input.clear()

    # def get_message_server(self):
    #     message_server = data
    #     self.chat_display.append('Server: ' + message_server)
    #     self.message_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = ChatApplication()
    chat_app.show()
    sys.exit(app.exec_())