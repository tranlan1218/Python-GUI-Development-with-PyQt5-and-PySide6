import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class ToolBars(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        exitaction = QAction(QIcon('exit.png'), 'Exit', self)
        exitaction.setShortcut('Ctrl+e')
        exitaction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitaction)
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Tool Bars Application Demo')
        self.show()

def main():
    app = QApplication(sys.argv)
    widget = ToolBars()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()