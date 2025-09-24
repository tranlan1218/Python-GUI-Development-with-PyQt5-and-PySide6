import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.namelabel = QLabel(self)
        self.namelabel.move(20, 50)
        self.namelabel.setText("Enter Your Name:")

        self.name = QLineEdit(self)
        self.name.move(120,48)
        self.name.show()

        submit = QPushButton(self)
        submit.setText("Submit")
        submit.move(150,80)
        submit.clicked.connect(self.showname)

    def showname(self):
        a = self.name.text()
        print(a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = App()
    widget.setGeometry(50, 50, 320, 300)
    widget.setWindowTitle('Line Edit Demo Application')
    widget.show()

    sys.exit(app.exec_())

    