from PySide6.QtCore import Qt
from widgets.custom_widgets import BasePanel
from settings.app_state import AppState
from settings.languages import lang_manager
from PySide6.QtWidgets import QLabel, QGridLayout



class TestPanel(BasePanel):
    def __init__(self):
        super().__init__()

        testPanel = QGridLayout()

        self.test = QLabel()
        self.test.setAlignment(Qt.AlignCenter)

        testPanel.addWidget(self.test)

        self.setLayout(testPanel)

        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )



    def updateLanguage(self):
        self.test.setText(
            lang_manager.get_text('coming_soon')
        )
        