import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget

os.environ['QT_QPA_PLATFORM'] = 'wayland'


app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()

if __name__ == '__main__':
    pass
