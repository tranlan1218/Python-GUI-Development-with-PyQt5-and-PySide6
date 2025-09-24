import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QPushButton

class Hobbies(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        label = QLabel(self)
        label.setText('Hobbies')
        label.move(65,20)

        hob1 = QCheckBox('Dancing', self)
        hob1.move(65,40)
        hob1.toggle()

        hob2 = QCheckBox('Singing', self)
        hob2.move(65,60)

        hob3 = QCheckBox('Reading', self)
        hob3.move(65,80)

        self.setGeometry(50, 50, 320, 300)
        self.setWindowTitle('Checkbox Application Demo')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cb = Hobbies()
    sys.exit(app.exec_())