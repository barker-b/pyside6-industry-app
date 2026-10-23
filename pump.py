import sys
from PySide6.QtCore import Qt
from widgets.custom_widgets import SecondPanel, DarkInput, DarkButton
from settings.languages import lang_manager
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
        self.speedInput = DarkInput()
        self.pressureInput = DarkInput()


        # Labels
        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                padding: 6px;
                }
        """)


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

        self.pump_flow = 0
        self.horse_power = 0
        self.required_torque = 0

        self.current_error = None

        self.updateOutputs()
        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )
        lang_manager.language_changed.connect(
            self.updateOutputs
        )


    def calculate(self):
        try:

            displacement = float(self.displacementInput.text())
            rpm = float(self.speedInput.text())
            pressure = float(self.pressureInput.text())

            if displacement < 0 or rpm < 0 or pressure < 0:
                self.current_error = 'negative_error'
                self.updateOutputs()
                return

            calc = PumpFormula(
                displacement=displacement,
                rpm=rpm,
                pressure=pressure
            )

            self.pump_flow = calc.output_flow()
            self.horse_power = calc.horse_power()
            self.required_torque = calc.torque()

            self.current_error = None

            self.updateOutputs()

        except ValueError:
            self.current_error = 'invalid_input'
            self.updateOutputs()



    def reset(self):
        self.displacementInput.clear()
        self.speedInput.clear()
        self.pressureInput.clear()

        self.pump_flow = 0
        self.horse_power = 0
        self.required_torque = 0
        self.current_error = None        

        self.updateOutputs()
        self.updateLanguage()

    def updateOutputs(self):

        if self.current_error:
            self.output.setText(
                lang_manager.get_text(
                    self.current_error
                )
            )
            return

        self.output.setText(
            f"{lang_manager.get_text('pump_flow')}"
            f" {self.pump_flow:,.0f} GPM"
            f"\n{lang_manager.get_text('horse_power')}"
            f" {self.horse_power:,.0f} HP"
            f"\n{lang_manager.get_text('required_torque')}"
            f" {self.required_torque:,.0f} lb-ft"
        )
        

    def updateLanguage(self):
        self.title.setText(
            lang_manager.get_text('pump')
        )
        self.calcButton.setText(
            lang_manager.get_text('calculate')
        )
        self.resetButton.setText(
            lang_manager.get_text('reset')
        )
        self.displacementInput.setPlaceholderText(
            lang_manager.get_text('displacement_hint')
        )
        self.speedInput.setPlaceholderText(
            lang_manager.get_text('speed_hint')
        )
        self.pressureInput.setPlaceholderText(
            lang_manager.get_text('pressure_hint')
        )
        
        