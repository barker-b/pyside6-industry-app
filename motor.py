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

from calculator import MotorFormula

class Motor(SecondPanel):
    def __init__(self):
        super().__init__()

        # Panel design
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)        


        # Input Boxes
        self.displacementInput = DarkInput()
        self.displacementInput.setPlaceholderText("Displacement (ci)")

        self.flowInput = DarkInput()
        self.flowInput.setPlaceholderText("flow (gpm)")

        self.pressureInput = DarkInput()
        self.pressureInput.setPlaceholderText("Pressure (psi)")

        # Labels
        self.title = QLabel("Motor")
        self.out_put = QLabel("Motor Torque: 0\n Motor Speed: 0")
        self.out_put.setAlignment(Qt.AlignCenter)
        self.out_put.setMinimumHeight(40)

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
        main_layout.addWidget(self.displacementInput)
        main_layout.addWidget(self.flowInput)
        main_layout.addWidget(self.pressureInput)
        main_layout.addWidget(self.out_put)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        self.calc_button.clicked.connect(self.calculate)
        self.reset_button.clicked.connect(self.reset)

    def calculate(self):
        try:
            displacement = float(self.displacementInput.text())
            flow = float(self.flowInput.text())
            pressure = float(self.pressureInput.text())

            calc = MotorFormula(
                displacement=displacement,
                flow=flow,
                pressure=pressure
            )

            torque = calc.motor_torque()
            motor_speed = calc.motor_speed()

            self.out_put.setText(
                f"Motor Torque: {torque:,.0f} ft-lbs.\n"
                f"Motor Speed: {motor_speed:,.0f} RPM."
            )

        except ValueError:
            self.out_put.setText("Error.")


    def reset(self):
        self.out_put.setText("Motor Torque: 0\n Motor Speed: 0")
        self.displacementInput.clear()
        self.flowInput.clear()
        self.pressureInput.clear()