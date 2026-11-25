import sys
from PySide6.QtCore import Qt
from widgets.custom_widgets import SecondPanel, ThemedInput, ThemedButton
from settings.languages import lang_manager
from settings.values import PUMP_VALUES
from calculator import PumpFormula
from graphs.pump_graph import PumpGraph
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QFrame
)


class Pump(SecondPanel):
    def __init__(self):
        super().__init__()

        # Panel design
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)        

        # Input Boxes
        self.displacementInput = ThemedInput()
        self.speedInput = ThemedInput()
        self.pressureInput = ThemedInput()

        # Labels
        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 30px;
                font-weight: bold;
                padding: 6px;
                }
        """)

        self.output = QLabel()
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setMinimumHeight(40)
        self.output.setStyleSheet("""
            QLabel {
                font-size: 20px;
                }
        """)

        # Inputs
        self.inputLayout = QVBoxLayout()
        self.inputLayout.setContentsMargins(50, 0, 50, 0)
        self.inputLayout.addWidget(self.displacementInput)
        self.inputLayout.addWidget(self.speedInput)
        self.inputLayout.addWidget(self.pressureInput)
        
        
        # Buttons
        self.calcButton = ThemedButton()
        self.resetButton = ThemedButton()

        # Button layout
        buttonLayout = QGridLayout()
        buttonLayout.setContentsMargins(25, 0, 25, 0)
        buttonLayout.addWidget(self.calcButton, 0, 0)
        buttonLayout.addWidget(self.resetButton, 0, 1)

        # Graph
        self.graph = PumpGraph()
        graphLayout = QVBoxLayout()
        graphLayout.addWidget(self.graph)

        # Window layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title)
        mainLayout.addLayout(self.inputLayout)
        mainLayout.addWidget(self.output)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addLayout(graphLayout)

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

            PUMP_VALUES['displacement'] = displacement
            PUMP_VALUES['speed'] = rpm
            PUMP_VALUES['pressure'] = pressure
            PUMP_VALUES['pump_flow'] = self.pump_flow
            PUMP_VALUES['horse_power'] = self.horse_power
            PUMP_VALUES['required_torque'] = self.required_torque

            self.current_error = None

            self.updateOutputs()

        except ValueError:
            self.current_error = 'invalid_input'
            self.updateOutputs()

        print(PUMP_VALUES)


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
        
        