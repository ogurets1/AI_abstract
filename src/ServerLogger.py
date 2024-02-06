from PyQt5.QtWidgets import QTextEdit

class ServerLogger:
    def __init__(self, text_edit):
        self.text_edit = text_edit

    def log(self, message):
        self.text_edit.append(message)

# Создание экземпляра QTextEdit
text_edit = QTextEdit()

# Создание экземпляра ServerLogger с передачей QTextEdit виджета
logger = ServerLogger(text_edit)

# Использование функции log для вывода сообщения в QTextEdit
logger.log('This is a log message')