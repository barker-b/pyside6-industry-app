import sys
from main_panels.hydraulic_panel import HydraulicsPanel
from main_panels.electrical_panel import ElectricPanel
from main_panels.formulas import FormulaPanel
from settings.app_state import AppState
from PySide6.QtCore import Qt
from settings.themes import THEMES
from settings.languages import lang_manager
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QToolBar,
    QStackedLayout,
    QComboBox,
    QToolButton,
    QMenu,
)
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indusrty Calculator")
        self.resize(1400, 900)

        # Menu Bar
        self.menu_bar = self.menuBar()

        file_menu = self.menu_bar.addMenu("&File")

        theme_menu = self.menu_bar.addMenu("&Themes")


        self.light_action = QAction(self)
        self.light_action.triggered.connect(
            lambda: self.setTheme('light')
        )
        self.dark_action = QAction("Dark", self)
        self.dark_action.triggered.connect(
            lambda: self.setTheme('dark')
        )
        self.blue_action = QAction("Blue", self)
        self.blue_action.triggered.connect(
            lambda: self.setTheme('blue')
        )

        themes = [self.light_action, self.dark_action, self.blue_action]

        for theme in themes:
            theme_menu.addAction(theme)

        # Tool bar
        self.tool_bar = QToolBar("Tools")
        self.tool_bar.setMovable(True)
        self.addToolBar(self.tool_bar)

        self.hydraulicsAction = QAction(self)
        self.hydraulicsAction.triggered.connect(
            lambda: self.stackLayout.setCurrentWidget(self.hydraulicPanel)
        )
        self.tool_bar.addAction(self.hydraulicsAction)

        self.electricalAction = QAction("Electrical", self)
        self.electricalAction.triggered.connect(
            lambda: self.stackLayout.setCurrentWidget(self.electricPanel)
        )      
        self.tool_bar.addAction(self.electricalAction)

        self.formulaAction = QAction("Formulas", self,)
        self.formulaAction.triggered.connect(
            lambda: self.stackLayout.setCurrentWidget(self.formulaPanel)
        )
        self.tool_bar.addAction(self.formulaAction)

        self.toggleUnitsAction = QAction("Metric", self)
        self.toggleUnitsAction.triggered.connect(self.toggleUnits)
        self.tool_bar.addAction(self.toggleUnitsAction)

        self.toggleLanguageAction = QAction("Spanish", self)
        self.toggleLanguageAction.triggered.connect(self.toggleLanguage)
        self.tool_bar.addAction(self.toggleLanguageAction)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Stacked layout
        self.stackLayout = QStackedLayout()
        central_widget.setLayout(self.stackLayout)

        # Pages
        self.hydraulicPanel = HydraulicsPanel()
        self.electricPanel = ElectricPanel()
        self.formulaPanel = FormulaPanel()

        self.stackLayout.addWidget(self.hydraulicPanel)
        self.stackLayout.addWidget(self.electricPanel)
        self.stackLayout.addWidget(self.formulaPanel)

        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )

    def setTheme(self, theme):
        AppState.theme = theme
        QApplication.instance().setStyleSheet(THEMES[theme])


    def toggleUnits(self):
        pass

    def toggleLanguage(self):
        if AppState.language == "en":
            AppState.language = "es"
            lang_manager.set_language('es')

        else:
            AppState.language = "en"
            lang_manager.set_language('en')



            
        print(AppState.language)

    

    def updateLanguage(self):
        self.light_action.setText(
            lang_manager.get_text('light')
        )
        self.dark_action.setText(
            lang_manager.get_text('dark')
        )
        self.blue_action.setText(
            lang_manager.get_text('blue')
        )
        self.hydraulicsAction.setText(
            lang_manager.get_text('hydraulics')
        )
        self.electricalAction.setText(
            lang_manager.get_text('electrical')
        )
        self.formulaAction.setText(
            lang_manager.get_text('formulas')
        )
        self.toggleUnitsAction.setText(
            lang_manager.get_text('metric')
        )
        if AppState.language == 'en':
            self.toggleLanguageAction.setText(
                lang_manager.get_text('spanish')
            )
        else:
            self.toggleLanguageAction.setText(
                lang_manager.get_text('english')
            )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet(THEMES[AppState.theme])
    window.show()
    sys.exit(app.exec())