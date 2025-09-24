import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QComboBox
#Providing a drop-down list of selectable items
class Price(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        price =QComboBox(self)
        price.addItem('100-200')        #add Item options into scroll box
        price.addItem('300-400')
        price.addItem('500-600')
        price.addItem('1000-1500')
        price.addItem('2500+')
        price.move(50,50)

        self.label = QLabel(self)
        self.label.move(50, 20)

        price.activated[str].connect(self.onChanged)

        self.setGeometry(50, 50, 300, 300)
        self.setWindowTitle('ComboBox Application Demo')

        self.show()


    def onChanged(self, Text):
        self.label.setText(Text)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Price()
    sys.exit(app.exec_())