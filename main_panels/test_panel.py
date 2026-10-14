from PySide6.QtCore import Qt
from widgets.custom_widgets import BasePanel
from settings.app_state import AppState
from settings.languages import LANGUAGE
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

class TestPanel(BasePanel):
    def __init__(self):
        super().__init__()

        testPanel = QGridLayout()

        self.test = QLabel(LANGUAGE[AppState.language]['greeting'])
        self.test.setAlignment(Qt.AlignCenter)

        testPanel.addWidget(self.test)

        self.setLayout(testPanel)

    def updateLanguage(self):
        self.test.setText(LANGUAGE[AppState.language]['greeting'])
        