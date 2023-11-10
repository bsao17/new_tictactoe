from PyQt5.QtWidgets import QMessageBox


def messages(self, title, message):
    """
    Returns a QMessageBox question with the given title and message.

    Parameters:
        self (object): The object instance.
        title (str): The title of the QMessageBox.
        message (str): The message to display in the QMessageBox.

    Returns:
        int: The user's response to the question.
    """
    return QMessageBox.question(self, title, message)
