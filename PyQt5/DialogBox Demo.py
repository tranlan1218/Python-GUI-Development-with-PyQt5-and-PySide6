import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLineEdit

class NameInput(QWidget):
    def __init__(self):

        QWidget.__init__(self)

        self.btn = QPushButton('Click Me', self)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.showDialog)

        self.name = QLineEdit(self)
        self.name.move(300, 100)

        self.setGeometry(300,300,450, 350)
        self.setWindowTitle('DialogBox Application Demo')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Name Dialog Box', 'Enter your name:')
        if ok:
            self.name.setText(str(text))

def main():
    app = QApplication(sys.argv)
    widget = NameInput()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
