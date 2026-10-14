from PySide6.QtCore import Qt
from electric_motor import ElectricMotor
from motor import Motor
from pump import Pump
from widgets.custom_widgets import BasePanel
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



        electricPanel = QGridLayout()
        electricTitle = QLabel("Electrical")
        electricTitle.setAlignment(Qt.AlignCenter)
        electricTitle.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            padding: 12px;
            """
        )
        electricTitle.setMaximumHeight(50)


        
        electricPanel.addWidget(electricTitle, 0, 0, 1, 2)
        electricPanel.addWidget(motorPanel, 1, 0)
        electricPanel.addWidget(motorPanel, 1 , 1)


        electricPanel.setColumnStretch(1, 1)

        self.setLayout(electricPanel)
