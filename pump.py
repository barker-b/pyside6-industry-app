import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QGridLayout,
    QFrame
)

class Pump(QFrame):
    def __init__(self):
        super().__init__()

        # Panel design
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)        

        # Input Boxes
        self.displacement_input = QLineEdit()
        self.displacement_input.setPlaceholderText("Displacement(ci)")

        self.speed_input = QLineEdit()
        self.speed_input.setPlaceholderText("Speed (rpm)")

        self.pressure_input = QLineEdit()
        self.pressure_input.setPlaceholderText("Pressure (psi)")

        # Labels
        self.title = QLabel("Pump")
        self.out_put = QLabel("Coming Soon!")
        
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                padding: 6px
                }
        """)


        # Buttons
        self.calc_button = QPushButton("Calculate")
        self.reset_button = QPushButton("Reset")

        # Button layout
        button_layout = QGridLayout()
        button_layout.addWidget(self.calc_button, 0, 0)
        button_layout.addWidget(self.reset_button, 0, 1)

        # Window layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title)
        main_layout.addWidget(self.displacement_input)
        main_layout.addWidget(self.speed_input)
        main_layout.addWidget(self.pressure_input)
        main_layout.addWidget(self.out_put)
        main_layout.addLayout(button_layout)


        self.setLayout(main_layout)
        