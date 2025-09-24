import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                               QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox,
                               QFrame, QLineEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPainter, QColor


class GridWidget(QFrame):
    def __init__(self, labels_bottom=None, parent=None):
        super().__init__(parent)
        self.labels_bottom = labels_bottom or []
        self.setMinimumSize(180, 160)
        self.setStyleSheet("background-color: white; border: 1px solid gray;")

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)
        qp.setPen(QColor(180, 180, 180))

        # Draw grid lines
        step_y = self.height() // 6
        step_x = self.width() // (len(self.labels_bottom) + 1)

        for i in range(1, 6):
            qp.drawLine(0, i * step_y, self.width(), i * step_y)
        for j in range(1, len(self.labels_bottom)):
            qp.drawLine(j * step_x, 0, j * step_x, self.height())

        # Draw bottom labels
        qp.setPen(Qt.black)
        font = QFont("Arial", 8)
        qp.setFont(font)
        for idx, lbl in enumerate(self.labels_bottom):
            qp.drawText((idx + 1) * step_x - 10, self.height() - 5, lbl)


class StateButton(QPushButton):
    def __init__(self, label="OFF"):
        super().__init__(label)
        self.state = "OFF"
        self.update_style()
        self.clicked.connect(self.toggle_state)

    def toggle_state(self):
        if self.state == "OFF":
            self.state = "ON"
        elif self.state == "ON":
            self.state = "ERROR"
        else:
            self.state = "OFF"
        self.update_style()

    def update_style(self):
        if self.state == "ON":
            self.setStyleSheet("background-color: green; color: white; font-weight: bold;")
            self.setText("ON")
        elif self.state == "OFF":
            self.setStyleSheet("background-color: gray; color: white; font-weight: bold;")
            self.setText("OFF")
        else:
            self.setStyleSheet("background-color: red; color: white; font-weight: bold;")
            self.setText("ERROR")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VLBI 장비 모니터링 시스템")
        self.setStyleSheet("background-color: #f0f4fa;")

        main_layout = QVBoxLayout(self)

        # --- Header ---
        header = QHBoxLayout()
        logo = QLabel("Logo")
        logo.setFixedSize(100, 60)
        logo.setStyleSheet("background-color:#2f5597; color:white; font:bold 16px; border:1px solid black;")
        header.addWidget(logo)

        title = QLabel("VLBI 장비 모니터링 시스템")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("background-color:#2f5597; color:white; font:bold 20px;")
        header.addWidget(title, stretch=1)

        datetime = QLabel("Date & Time")
        datetime.setFixedSize(120, 60)
        datetime.setStyleSheet("background-color:lightblue; border:1px solid black; font:12px;")
        header.addWidget(datetime)
        main_layout.addLayout(header)

        status = QLabel("Working status")
        status.setAlignment(Qt.AlignCenter)
        status.setStyleSheet("background-color:white; border:1px solid gray;")
        main_layout.addWidget(status)

        # --- Top converters ---
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.make_group("S/X DownConverter", ["S", "X1", "X2"]))
        top_layout.addWidget(self.make_group("K DownConverter", ["K1", "K2", "K3", "K4"]))
        top_layout.addWidget(self.make_group("Q DownConverter", ["Q1", "Q2", "Q3", "Q4"]))
        top_layout.addWidget(self.make_group("Video Converter", ["CH2","CH4","CH6","CH8","CH10","CH12","CH14","CH16"]))
        main_layout.addLayout(top_layout)

        # --- Bottom ---
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.make_group("ACU", []))
        bottom_layout.addWidget(self.make_group("2/8GHz Switch", []))
        bottom_layout.addWidget(self.make_group("Noise Diode", []))
        bottom_layout.addWidget(self.make_group("Pol Selector", []))
        bottom_layout.addWidget(self.make_group("IF Selector", ["CH2","CH4","CH6","CH8","CH10","CH12","CH14","CH16"]))
        main_layout.addLayout(bottom_layout)

        # --- Alarm logs ---
        alarm_box = QLabel("Alarm logs")
        alarm_box.setAlignment(Qt.AlignCenter)
        alarm_box.setFixedHeight(50)
        alarm_box.setStyleSheet("background-color:#d9e1f2; border:1px solid gray; font-weight:bold;")
        main_layout.addWidget(alarm_box)

    def make_group(self, title, labels_bottom):
        box = QGroupBox(title)
        box.setStyleSheet("QGroupBox { font-weight:bold; color:white; background-color:#2f5597; border:1px solid gray; }")
        layout = QVBoxLayout(box)
        grid = GridWidget(labels_bottom)
        layout.addWidget(grid)
        return box


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(1200, 700)
    win.show()
    sys.exit(app.exec())
