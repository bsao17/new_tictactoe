from PyQt5.QtWidgets import QMessageBox


class Messages:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def information_message(self):
        """
        Displays an information message box with the given title and message.
        """
        QMessageBox.information(self.title, self.message)