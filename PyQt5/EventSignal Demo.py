import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QLineEdit,QVBoxLayout, QApplication, QSlider

class SignalDemo(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        LCD = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(LCD)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        slider.valueChanged.connect(LCD.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal Demo')
        self.show()

def main():
    app = QApplication(sys.argv)
    widget = SignalDemo()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()