import sys
from main_panels.hydraulic_panel import HydraulicsPanel
from main_panels.electrical_panel import ElectricPanel
from main_panels.test_panel import TestPanel
from main_panels.angle_panel import AnglePanel
from settings.app_state import AppState
from motor import Motor
from pump import Pump
from PySide6.QtCore import Qt
from settings.themes import THEMES
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
)
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indusrty Calculator")
        self.resize(800, 800)

        # Tool bar
        self.tool_bar = QToolBar("Tools")
        self.tool_bar.setMovable(False)
        self.addToolBar(self.tool_bar)

        self.toggleThemeAction = QAction("Dark Theme", self)
        self.toggleThemeAction.triggered.connect(self.toggleTheme)
        self.tool_bar.addAction(self.toggleThemeAction)

        self.toggleUnitsAction = QAction("Metric", self)
        self.toggleUnitsAction.triggered.connect(self.toggleUnits)
        self.tool_bar.addAction(self.toggleUnitsAction)

        self.toggleLanguageAction = QAction("Spanish", self)
        self.toggleLanguageAction.triggered.connect(self.toggleLanguage)
        self.tool_bar.addAction(self.toggleLanguageAction)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Layout
        mainLayout = QGridLayout()
        central_widget.setLayout(mainLayout)

        # Panels
        hydraulic_Panel = HydraulicsPanel()
        electric_Panel = ElectricPanel()
        angle_panel = AnglePanel()
        test_panel_right = TestPanel()


        mainLayout.addWidget(hydraulic_Panel, 0, 0)
        mainLayout.addWidget(electric_Panel, 0, 1)
        mainLayout.addWidget(angle_panel, 1, 0)
        mainLayout.addWidget(test_panel_right, 1, 1)


        mainLayout.setRowStretch(1, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)

    def toggleTheme(self):
        if AppState.theme == "light":
            AppState.theme = "dark"
            QApplication.instance().setStyleSheet(THEMES[AppState.theme])
            self.toggleThemeAction.setText("Light Theme")


        else:
            AppState.theme = "light"
            QApplication.instance().setStyleSheet(THEMES[AppState.theme])
            self.toggleThemeAction.setText("Dark Theme")

    def toggleUnits(self):
        pass

    def toggleLanguage(self):
        if AppState.language == "en":
            AppState.language = "es"

            lang_manager.set_language('es')

            self.toggleLanguageAction.setText("Inglés")

        else:
            AppState.language = "en"

            lang_manager.set_language('en')

            self.toggleLanguageAction.setText("Spanish")

            
        print(AppState.language)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet(THEMES[AppState.theme])
    window.show()
    sys.exit(app.exec())