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
        self.output = QLabel("Motor Torque: 0\n Motor Speed: 0")
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setMinimumHeight(40)

        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                padding: 6px
                }
        """)


        # Buttons

        self.calcButton = DarkButton()
        self.calcButton.setText("Calculate")
        self.resetButton = DarkButton()
        self.resetButton.setText("Reset")

        #Button Layout
        buttonLayout = QGridLayout()
        buttonLayout.addWidget(self.calcButton, 0, 0)
        buttonLayout.addWidget(self.resetButton, 0, 1)

        # Main screen layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title)
        mainLayout.addWidget(self.displacementInput)
        mainLayout.addWidget(self.flowInput)
        mainLayout.addWidget(self.pressureInput)
        mainLayout.addWidget(self.output)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)

        self.calcButton.clicked.connect(self.calculate)
        self.resetButton.clicked.connect(self.reset)

    def calculate(self):
        try:
            displacement = float(self.displacementInput.text())
            flow = float(self.flowInput.text())
            pressure = float(self.pressureInput.text())

            if displacement < 0 or flow < 0 or pressure < 0:
                self.output.setText(
                    "Invalid, inputs must be\n"
                    "positive numbers"
                )
                return

            calc = MotorFormula(
                displacement=displacement,
                flow=flow,
                pressure=pressure
            )

            torque = calc.motor_torque()
            motor_speed = calc.motor_speed()

            self.output.setText(
                f"Motor Torque: {torque:,.0f} ft-lbs.\n"
                f"Motor Speed: {motor_speed:,.0f} RPM."
            )

        except ValueError:
            self.output.setText("Error.")


    def reset(self):
        self.output.setText("Motor Torque: 0\n Motor Speed: 0")
        self.displacementInput.clear()
        self.flowInput.clear()
        self.pressureInput.clear()