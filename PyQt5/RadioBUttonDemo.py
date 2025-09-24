from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QGridLayout
import sys

class RadioDemo(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        radio = QRadioButton('Male')
        radio.setChecked(True)
        radio.gender = 'Male'
        radio.toggled.connect(self.onClicked)
        layout.addWidget(radio, 0, 0)


        radio = QRadioButton('Female')
        radio.gender = 'Female'
        radio.toggled.connect(self.onClicked)
        layout.addWidget(radio, 0, 1)

        radio = QRadioButton('Others')
        radio.gender = 'Others'
        radio.toggled.connect(self.onClicked)
        layout.addWidget(radio, 0, 2)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print('Genfer is %s' % (radioButton.gender))


app = QApplication(sys.argv)

widget = RadioDemo()
widget.setWindowTitle('Radio Button Demo Application')
widget.show()
sys.exit(app.exec_())

