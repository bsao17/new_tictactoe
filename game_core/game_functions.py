from PyQt5.QtWidgets import QMessageBox


def messages(self, title, message):
    return QMessageBox.question(self, title, message)
