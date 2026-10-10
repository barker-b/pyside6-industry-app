import sys
from main_panels.hydraulic_panel import HydraulicsPanel
from motor import Motor
from pump import Pump
from PySide6.QtCore import Qt
from settings.themes import THEMES
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

class AppState:
    theme = "light"
    language = "en"
    units = "sae"


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


        # Placeholders for now
        hydraulic_Panel = HydraulicsPanel()
        electricLabel = QLabel("Electrical Coming Soon!")
        fluidsLabel = QLabel("Fluids Coming Soon!")
        materialsLabel = QLabel("Materials Coming Soon!")
        extraPanel = QLabel("Coming soon!")
        extraPanel.setAlignment(Qt.AlignCenter)
    
        electricPanel = QGridLayout()
        electricPanel.addWidget(electricLabel)
        electricLabel.setAlignment(Qt.AlignCenter)

        fluidsPanel = QGridLayout()
        fluidsPanel.addWidget(fluidsLabel)
        fluidsLabel.setAlignment(Qt.AlignCenter)

        materialsPanel = QGridLayout()
        materialsPanel.addWidget(materialsLabel)
        materialsLabel.setAlignment(Qt.AlignCenter)

        mainLayout.addWidget(hydraulic_Panel, 0, 0)
        mainLayout.addLayout(electricPanel, 0, 1)
        mainLayout.addLayout(fluidsPanel, 1, 0)
        mainLayout.addLayout(materialsPanel, 1, 1)


        mainLayout.setRowStretch(1, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)

    def toggleTheme(self):
        if AppState.theme == "light":
            AppState.theme = "dark"
            QApplication.instance().setStyleSheet(THEMES[AppState.theme])
            self.toggleThemeAction.setText("Dark Theme")


        else:
            AppState.theme = "light"
            QApplication.instance().setStyleSheet(THEMES[AppState.theme])
            self.toggleThemeAction.setText("Light Theme")

    def toggleUnits(self):
        pass

    def toggleLanguage(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet(THEMES[AppState.theme])
    window.show()
    sys.exit(app.exec())