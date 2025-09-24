import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QMenuBar, QAction

class TextPad(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Status Shown')

        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')
        editmenu = menubar.addMenu('Edit')
        fontmenu = menubar.addMenu('Font')
        viewmenu = menubar.addMenu('View')


        viewaction = QAction('View Status Bar', self, checkable=True)
        viewaction.setStatusTip('View Status Bar')
        viewaction.setChecked(True)
        viewaction.triggered.connect(self.showhide)

        viewmenu.addAction(viewaction)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("MenuBar Application Demo")
        self.show()

    def showhide(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

def main():
    app = QApplication(sys.argv)
    textpad = TextPad()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    