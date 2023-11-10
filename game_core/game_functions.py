from PyQt5.QtWidgets import QMessageBox


def messages(self, title, message):
    """
    Displays an information message box with the given title and message.

    Parameters:
        self (QWidget): The parent widget.
        title (str): The title of the message box.
        message (str): The message to be displayed.

    Returns:
        int: The result of the message box button clicked (QMessageBox.Ok).
    """
    return QMessageBox.information(self, title, message, QMessageBox.Ok)
