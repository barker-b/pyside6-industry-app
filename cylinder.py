import sys
from PySide6.QtCore import Qt
from widgets.custom_widgets import SecondPanel, DarkInput, DarkButton
from PySide6.QtWidgets import (
    QMainWindow,
    QFrame,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)

from calculator import CylFormula


class Cylinder(SecondPanel):
    def __init__(self):
        super().__init__()

        # Input Boxes
        self.boreInput = DarkInput()
        self.boreInput.setPlaceholderText("Bore Size (in)")


        self.rodInput = DarkInput()
        self.rodInput.setPlaceholderText("Rod Size (in)")

        self.pressureInput = DarkInput()
        self.pressureInput.setPlaceholderText("Pressure (psi)")

        # Labels
        self.title = QLabel("Cylinder")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            padding: 6px;
            """
        )

        self.output = QLabel("Push Force: 0 \nPull Force: 0 ")
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
        
        # Main screen layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title)
        mainLayout.addWidget(self.boreInput)
        mainLayout.addWidget(self.rodInput)
        mainLayout.addWidget(self.pressureInput)
        mainLayout.addWidget(self.output)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)

        self.calcButton.clicked.connect(self.calculate)
        self.resetButton.clicked.connect(self.reset)

    def calculate(self):
        try:
            bore = float(self.boreInput.text())
            rod = float(self.rodInput.text())
            pressure = float(self.pressureInput.text())

            if rod >= bore:
                self.output.setText(
                    "Invalid, rod cannot be\n"
                    "the same or larger than bore"
                )
                return

            if rod < 0 or bore < 0 or pressure < 0:
                self.output.setText(
                    "Invalid, inputs must be\n"
                    "positive numbers"
                )
                return

            calc = CylFormula(
                bore=bore,
                rod=rod,
                pressure=pressure
            )

            push = calc.cyl_ext_force()
            pull = calc.cyl_ret_force()

            self.output.setText(
                f"Push Force: {push:,.0f} pounds.\n"
                f"Pull Force: {pull:,.0f} pounds."
            )
            
        except ValueError:
            self.output.setText("Error.")

    def reset(self):
        self.output.setText("Push Force: 0 \nPull Force: 0")
        self.boreInput.clear()
        self.rodInput.clear()
        self.pressureInput.clear()






