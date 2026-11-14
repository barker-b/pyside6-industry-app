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

        self.file_menu = self.menu_bar.addMenu("&File")
        self.language_menu = self.menu_bar.addMenu("&Language")
        self.theme_menu = self.menu_bar.addMenu("&Themes")
        self.unit_menu = self.menu_bar.addMenu("&Units")

        # Language actions
        self.english_action = QAction(self)
        self.english_action.triggered.connect(
            lambda: self.set_language('en')
        )
        self.spanish_action = QAction(self)
        self.spanish_action.triggered.connect(
            lambda: self.set_language('es')
        )
        self.german_action = QAction(self)
        self.german_action.triggered.connect(
            lambda: self.set_language('de')
        )
        self.russian_action = QAction(self)
        self.russian_action.triggered.connect(
            lambda: self.set_language('ru')
        )
        self.chinese_action = QAction(self)
        self.chinese_action.triggered.connect(
            lambda: self.set_language('zh-Hans')
        )

        self.language_menu.addAction(self.english_action)
        self.language_menu.addAction(self.spanish_action)
        self.language_menu.addAction(self.german_action)
        self.language_menu.addAction(self.russian_action)
        self.language_menu.addAction(self.chinese_action)
        
        # Theme actions
        self.light_action = QAction(self)
        self.light_action.triggered.connect(
            lambda: self.setTheme('light')
        )
        self.dark_action = QAction(self)
        self.dark_action.triggered.connect(
            lambda: self.setTheme('dark')
        )
        self.blue_action = QAction(self)
        self.blue_action.triggered.connect(
            lambda: self.setTheme('blue')
        )

        self.theme_menu.addAction(self.light_action)
        self.theme_menu.addAction(self.dark_action)
        self.theme_menu.addAction(self.blue_action)

        # Unit actions
        self.standard_action = QAction("Dumb", self)
        self.metric_action = QAction("Metric", self)

        self.unit_menu.addAction(self.standard_action)
        self.unit_menu.addAction(self.metric_action)
        

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

    def set_language(self, language):
        AppState.language = language
        lang_manager.set_language(language)


    def set_units(self):
        pass


    menus = {}

    actions = {}
    
    def updateLanguage(self):
        self.file_menu.setTitle(
            lang_manager.get_text('file')
        )
        self.language_menu.setTitle(
            lang_manager.get_text('language')
        )
        self.theme_menu.setTitle(
            lang_manager.get_text('theme')
        )
        self.unit_menu.setTitle(
            lang_manager.get_text('units')
        )
        self.english_action.setText(
            lang_manager.get_text('english')
        )
        self.spanish_action.setText(
            lang_manager.get_text('spanish')
        )
        self.german_action.setText(
            lang_manager.get_text('german')
        )
        self.russian_action.setText(
            lang_manager.get_text('russian')
        )
        self.chinese_action.setText(
            lang_manager.get_text('chinese')
        )
        self.standard_action.setText(
            lang_manager.get_text('dumb')
        )
        self.metric_action.setText(
            lang_manager.get_text('metric')
        )
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet(THEMES[AppState.theme])
    window.show()
    sys.exit(app.exec())