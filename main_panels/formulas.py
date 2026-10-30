from PySide6.QtCore import Qt
from widgets.custom_widgets import BasePanel, SecondPanel
from settings.languages import lang_manager
from PySide6.QtWidgets import QLabel, QGridLayout, QVBoxLayout


class FormulaPanel(BasePanel):
    def __init__(self):
        super().__init__()


        title = QLabel("Formulas")
        title.setAlignment(Qt.AlignCenter)
        title.setMaximumHeight(60)
        title.setStyleSheet(
            """
            font-size: 50px;
            font-weight: bold;
            """
        )

        hydraulic_formulas = SecondPanel()
        electric_formulas = SecondPanel()

        layout = QGridLayout()

        layout.addWidget(title, 0, 0, 1, 2)
        layout.addWidget(hydraulic_formulas, 1, 0)
        layout.addWidget(electric_formulas, 1, 1)

        self.setLayout(layout)







