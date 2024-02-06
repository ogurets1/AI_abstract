import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLineEdit
import socket
import threading
import server
class ServerControlProgram(QWidget):


    def __init__(self,text_edit):
        super().__init__()
        self.init_ui()
        self.text_edit = text_edit



    def init_ui(self):
        self.setWindowTitle('Server Control Program')
        self.setGeometry(100, 100, 400, 300)

        self.start_button = QPushButton('Start Server', self)
        self.start_button.clicked.connect(self.start_server)

        self.stop_button = QPushButton('Stop Server', self)
        self.stop_button.clicked.connect(self.stop_server)

        self.chat_box = QTextEdit()
        self.command_line = QLineEdit()
        self.command_line.returnPressed.connect(self.send_command)
        self.chat_box.append(self.communication_server)
        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.chat_box)
        layout.addWidget(self.command_line)

        self.setLayout(layout)



    def start_server(self):
        self.chat_box.append('Server started')
        server.main()

    def stop_server(self):
        self.chat_box.append('Server stopped')

    def log(self, message):
        self.chat_box.append(message)


    def send_command(self):
        command = self.command_line.text()
        self.chat_box.append('Command: ' + command)

        self.command_line.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ServerControlProgram()
    window.show()

    sys.exit(app.exec_())