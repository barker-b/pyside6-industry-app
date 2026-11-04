from PySide6.QtCore import Qt
from widgets.custom_widgets import BasePanel, SecondPanel
from settings.languages import lang_manager
from PySide6.QtWidgets import QLabel, QGridLayout, QVBoxLayout


class FormulaPanel(BasePanel):
    def __init__(self):
        super().__init__()


        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setMaximumHeight(60)
        self.title.setStyleSheet(
            """
            font-size: 50px;
            font-weight: bold;
            """
        )

        hydraulic_formulas = SecondPanel()
        electric_formulas = SecondPanel()

        layout = QGridLayout()

        layout.addWidget(self.title, 0, 0, 1, 2)
        layout.addWidget(hydraulic_formulas, 1, 0)
        layout.addWidget(electric_formulas, 1, 1)



        self.setLayout(layout)

        self.updateLanguage()

        lang_manager.language_changed.connect(
            self.updateLanguage
        )

    def updateLanguage(self):
        self.title.setText(
            lang_manager.get_text('formulas')
        )








