import sys
from PySide6.QtCore import Qt
from widgets.custom_widgets import SecondPanel, DarkInput, DarkButton
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QFrame,
    QGridLayout,
)

class Motor(SecondPanel):
    def __init__(self):
        super().__init__()

        # Panel design
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)        


        # Input Boxes
        self.displacement_input = DarkInput()
        self.displacement_input.setPlaceholderText("Displacement (ci)")

        self.flow_input = DarkInput()
        self.flow_input.setPlaceholderText("flow (gpm)")

        self.pressure_input = DarkInput()
        self.pressure_input.setPlaceholderText("Pressure (psi)")

        # Labels
        self.title = QLabel("Motor")
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

        self.calc_button = DarkButton()
        self.calc_button.setText("Calculate")
        self.reset_button = DarkButton()
        self.reset_button.setText("Reset")

        #Button Layout
        button_layout = QGridLayout()
        button_layout.addWidget(self.calc_button, 0, 0)
        button_layout.addWidget(self.reset_button, 0, 1)

        # Main screen layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title)
        main_layout.addWidget(self.displacement_input)
        main_layout.addWidget(self.flow_input)
        main_layout.addWidget(self.pressure_input)
        main_layout.addWidget(self.out_put)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)