from PySide6.QtCore import Qt
from electric_panels.electric_motor import ElectricMotor
from motor import Motor
from pump import Pump
from widgets.custom_widgets import BasePanel, SecondPanel
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
    QToolBar,
    QFrame,
)

class ElectricPanel(BasePanel):
    def __init__(self):
        super().__init__()

        motorPanel = ElectricMotor()
        extra1 = SecondPanel()
        extra2 = SecondPanel()
        extra3 = SecondPanel()




        electricPanel = QGridLayout()
        self.electricTitle = QLabel()
        self.electricTitle.setAlignment(Qt.AlignCenter)
        self.electricTitle.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            """
        )
        self.electricTitle.setMaximumHeight(50)


        
        electricPanel.addWidget(self.electricTitle, 0, 0, 1, 2)
        electricPanel.addWidget(motorPanel, 1, 0)
        electricPanel.addWidget(extra1, 1, 1)
        electricPanel.addWidget(extra2, 2, 0)
        electricPanel.addWidget(extra3, 2, 1)


        electricPanel.setColumnStretch(1, 1)
        electricPanel.setColumnStretch(0, 1)

        self.setLayout(electricPanel)

        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )

    def updateLanguage(self):
        self.electricTitle.setText(
            lang_manager.get_text('electrical')
        )



        
    
