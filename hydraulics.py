import sys
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)


class Hydraulics(QWidget):
    def __init__(self):
        super().__init__()


        # Input Boxes
        self.bore_input = QLineEdit()
        self.bore_input.setPlaceholderText("Bore Size (in)")

        self.rod_input = QLineEdit()
        self.rod_input.setPlaceholderText("Rod Size (in)")

        self.pressure_input = QLineEdit()
        self.pressure_input.setPlaceholderText("Pressure (psi)")

        # Labels
        self.out_put = QLabel("Coming Soon!")

        # Buttons
        self.calc_button = QPushButton("Calculate")


        
        # Main screen layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.bore_input)
        main_layout.addWidget(self.rod_input)
        main_layout.addWidget(self.pressure_input)
        main_layout.addWidget(self.out_put)
        main_layout.addWidget(self.calc_button)

        self.setLayout(main_layout)

