import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

class SliderDemo(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Slider Application Demo")
        self.setGeometry(300, 300, 400, 300)

        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.sliderdata)

        self.slidervalue = QLabel("0")
        self.slidervalue.setFont(QtGui.QFont("senserif", 18))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.slidervalue)

        self.setLayout(hbox)
        self.show()

    def sliderdata(self):
        size = self.slider.value()
        self.slidervalue.setText(str(size))

app = QApplication(sys.argv)
wdget = SliderDemo()
sys.exit(app.exec_())
