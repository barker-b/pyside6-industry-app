import sys
from PySide6.QtCore import Qt
from widgets.custom_widgets import SecondPanel, DarkInput, DarkButton
from settings.languages import lang_manager
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
        self.rodInput = DarkInput()
        self.pressureInput = DarkInput()


        # Labels
        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            padding: 6px;
            """
        )

        self.output = QLabel()
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setMinimumHeight(40)

        # Buttons
        self.calcButton = DarkButton()
        self.resetButton = DarkButton()


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

        self.push = 0
        self.pull = 0

        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )


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

            self.push = calc.cyl_ext_force()
            self.pull = calc.cyl_ret_force()

            self.updateLanguage()

            
        except ValueError:
            self.output.setText("Error.")



    def reset(self):
        self.boreInput.clear()
        self.rodInput.clear()
        self.pressureInput.clear()

        self.push = 0
        self.pull = 0

        self.updateLanguage()

    def updateLanguage(self):

        self.title.setText(
            lang_manager.get_text('cylinder')
        )
        self.calcButton.setText(
            lang_manager.get_text('calculate')
        )
        self.resetButton.setText(
            lang_manager.get_text('reset')
        )
        self.output.setText(
            f"{lang_manager.get_text('push_force')} {self.push:,.0f} "
            f" {lang_manager.get_text('pounds')}\n"
            f"{lang_manager.get_text('pull_force')} {self.pull:,.0f} "
            f" {lang_manager.get_text('pounds')}"
        )
        self.boreInput.setPlaceholderText(
            lang_manager.get_text('bore_hint')
        )
        self.rodInput.setPlaceholderText(
            lang_manager.get_text('rod_hint')
        )
        self.pressureInput.setPlaceholderText(
            lang_manager.get_text('pressure_hint')
        )











