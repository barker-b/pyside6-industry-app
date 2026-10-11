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
    QGridLayout,
    QFrame
)

from calculator import PumpFormula

class Pump(SecondPanel):
    def __init__(self):
        super().__init__()

        # Panel design
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)        

        # Input Boxes
        self.displacementInput = DarkInput()
        self.displacementInput.setPlaceholderText("Displacement(ci)")

        self.speedInput = DarkInput()
        self.speedInput.setPlaceholderText("Speed (rpm)")

        self.pressureInput = DarkInput()
        self.pressureInput.setPlaceholderText("Pressure (psi)")

        # Labels
        self.title = QLabel("Pump")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                padding: 6px;
                }
        """)


        self.output = QLabel(
            "Pump Output: 0 GPM.\n"
            "Horsepower: 0 HP.\n"
            "Driving Torque Required: 0 ft-lbs."
        )
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setMinimumHeight(40)
        


        # Buttons
        self.calcButton = DarkButton()
        self.calcButton.setText("Calculate")
        self.resetButton = DarkButton()
        self.resetButton.setText("Reset")

        # Button layout
        buttonLayout = QGridLayout()
        buttonLayout.addWidget(self.calcButton, 0, 0)
        buttonLayout.addWidget(self.resetButton, 0, 1)

        # Window layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title)
        mainLayout.addWidget(self.displacementInput)
        mainLayout.addWidget(self.speedInput)
        mainLayout.addWidget(self.pressureInput)
        mainLayout.addWidget(self.output)
        mainLayout.addLayout(buttonLayout)


        self.setLayout(mainLayout)

        self.calcButton.clicked.connect(self.calculate)
        self.resetButton.clicked.connect(self.reset)


    def calculate(self):
        try:

            displacement = float(self.displacementInput.text())
            rpm = float(self.speedInput.text())
            pressure = float(self.pressureInput.text())

            calc = PumpFormula(
                displacement=displacement,
                rpm=rpm,
                pressure=pressure
            )

            pumpFlow = calc.output_flow()
            horsePower = calc.horse_power()
            torque = calc.torque()

            self.output.setText(
                f"Pump Output: {pumpFlow:,.0f} GPM.\n"
                f"Pump Horsepower: {horsePower:,.0f} HP.\n"
                f"Driving Torque Required: {torque:,.0f} ft-lbs."
            )
        

        except ValueError:
            self.output.setText("Error.")


    def reset(self):
        self.output.setText(
            "Pump Output: 0 GPM.\n"
            "Horsepower: 0 HP.\n"
            "Driving Torque Required: 0 ft-lbs."            
        )
        self.displacementInput.clear()
        self.speedInput.clear()
        self.pressureInput.clear()
        
        