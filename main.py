import sys
from hydraulics import Hydraulics
from motors import Motor
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QGridLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indusrty Calculator")
        self.resize(400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        hyd_screen = Hydraulics()
        motor_wig = Motor()


        layout.addWidget(hyd_screen, 0, 0)
        layout.addWidget(motor_wig, 0, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())