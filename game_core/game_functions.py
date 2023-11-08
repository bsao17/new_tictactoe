from PyQt5.QtWidgets import QMessageBox


def messages(self, title, message):
    return QMessageBox.information(self, title, message)
