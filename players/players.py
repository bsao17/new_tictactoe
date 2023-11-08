from PyQt5.QtWidgets import QMessageBox


def messages(message: str):
    return QMessageBox(message)


class Players:
    def __init__(self, username):
        self.username = username
