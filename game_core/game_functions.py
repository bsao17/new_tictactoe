from PyQt5.QtWidgets import QMessageBox


def messages(title, message):
    """
    Displays an information message box with the given title and message.
    """
    #return QMessageBox.information(self, title, message, QMessageBox.Ok)
    print(title, message)
