import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from gui.alarm_popup import AlarmPopup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI from Qt Designer file
        ui_file = QFile("main_window.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setCentralWidget(self.ui)

        # Connect GUI buttons to actions
        self.ui.btnSetThreshold.clicked.connect(self.set_threshold)
        self.ui.btnTestAlarm.clicked.connect(self.test_alarm)

        # Example threshold storage
        self.threshold = None

    def set_threshold(self):
        """Store user-defined threshold value"""
        try:
            value = float(self.ui.inputThreshold.text())
            self.threshold = value
            self.ui.lblStatus.setText(f"Threshold set: {value}")
        except ValueError:
            self.ui.lblStatus.setText("Invalid input!")

    def test_alarm(self):
        """Simulate an alarm trigger"""
        popup = AlarmPopup("Threshold exceeded!", self)
        popup.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())