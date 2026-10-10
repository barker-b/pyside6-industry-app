from PySide6.QtCore import Qt
from cylinder import Cylinder
from motors import Motor
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

class HydraulicsPanel(BasePanel):
    def __init__(self):
        super().__init__()

        cylPanel = Cylinder()
        motorPanel = Motor()
        pumpPanel = Pump()
        extraPanel = QLabel("Coming soon!")
        extraPanel.setAlignment(Qt.AlignCenter)

        hydraulicsPanel = QGridLayout()
        hydTitle = QLabel("Hydraulics")
        hydTitle.setAlignment(Qt.AlignCenter)
        hydTitle.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            padding: 12px;
            """
        )


        
        hydraulicsPanel.addWidget(hydTitle, 0, 0, 1, 2)
        hydraulicsPanel.addWidget(cylPanel, 1, 0)
        hydraulicsPanel.addWidget(motorPanel, 1 , 1)
        hydraulicsPanel.addWidget(pumpPanel, 2, 0)

        hydraulicsPanel.setColumnStretch(1, 1)

        self.setLayout(hydraulicsPanel)


