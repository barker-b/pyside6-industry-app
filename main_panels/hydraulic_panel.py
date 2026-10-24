from PySide6.QtCore import Qt
from hydraulics.cylinder import Cylinder
from hydraulics.motor import Motor
from hydraulics.pump import Pump
from widgets.custom_widgets import BasePanel
from settings.languages import lang_manager
from PySide6.QtWidgets import QLabel, QGridLayout

class HydraulicsPanel(BasePanel):
    def __init__(self):
        super().__init__()


        cylPanel = Cylinder()
        motorPanel = Motor()
        pumpPanel = Pump()

        self.extraPanel = QLabel()
        self.extraPanel.setAlignment(Qt.AlignCenter)

        hydraulicsLayout = QGridLayout()
        self.hydTitle = QLabel()
        self.hydTitle.setAlignment(Qt.AlignCenter)
        self.hydTitle.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            """
        )
        self.hydTitle.setMaximumHeight(50)

        
        hydraulicsLayout.addWidget(self.hydTitle, 0, 0, 1, 2)
        hydraulicsLayout.addWidget(cylPanel, 1, 0, 2, 1)
        hydraulicsLayout.addWidget(motorPanel, 1, 1)
        hydraulicsLayout.addWidget(pumpPanel, 2, 1)


        hydraulicsLayout.setColumnStretch(0, 1)
        hydraulicsLayout.setColumnStretch(1, 1)

        self.setLayout(hydraulicsLayout)

        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )

        

    def updateLanguage(self):
        self.hydTitle.setText(
            lang_manager.get_text('hydraulics')
        )
        self.extraPanel.setText(
            lang_manager.get_text('coming_soon')
        )


        







