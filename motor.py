import sys
from PySide6.QtCore import Qt
from widgets.custom_widgets import SecondPanel, DarkInput, DarkButton
from settings.languages import lang_manager
from settings.app_state import AppState
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
        self.flowInput = DarkInput()
        self.pressureInput = DarkInput()


        # Labels
        self.title = QLabel()
        self.output = QLabel()
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
        self.resetButton = DarkButton()

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
        
        self.motor_torque = 0
        self.motor_speed = 0         

        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )

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

            self.motor_torque = calc.motor_torque()
            self.motor_speed = calc.motor_speed()

            self.updateLanguage()



        except ValueError:
            self.output.setText("Error.")


    def reset(self):
        self.displacementInput.clear()
        self.flowInput.clear()
        self.pressureInput.clear()

        self.motor_torque = 0
        self.motor_speed = 0

        self.updateLanguage()

    def updateLanguage(self):
        if AppState.language == "es":
            self.title.setText(
                f"{lang_manager.get_text('motor')}\n"
                f"{lang_manager.get_text('hydraulics_masculine')}"
            )
        else:
            self.title.setText(
                f"{lang_manager.get_text('hydraulic')}\n"
                f"{lang_manager.get_text('motor')}"
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
        self.flowInput.setPlaceholderText(
            lang_manager.get_text('flow_hint')
        )
        self.pressureInput.setPlaceholderText(
            lang_manager.get_text('pressure_hint')
        )
        self.output.setText(
            f"{lang_manager.get_text('motor_torque')} {self.motor_torque:,.0f}"
            f" {'lb-ft'}\n"
            f"{lang_manager.get_text('motor_speed')} {self.motor_speed:,.0f}"
            f" {'RPM'}"
        )
