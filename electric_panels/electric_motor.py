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

class ElectricMotor(SecondPanel):
    def __init__(self):
        super().__init__()

        self.voltageInput = DarkInput()
        self.ampsInput = DarkInput()
        self.phaseInput = DarkInput()


        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            """   
        )
        self.title.setMaximumHeight(50)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title)
        mainLayout.addWidget(self.voltageInput)
        mainLayout.addWidget(self.ampsInput)    
        mainLayout.addWidget(self.phaseInput)


        self.setLayout(mainLayout)

        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )

    def updateLanguage(self):
        self.title.setText(
            lang_manager.get_text('electrical_motor')
        )

