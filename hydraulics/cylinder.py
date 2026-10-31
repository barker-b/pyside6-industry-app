from PySide6.QtCore import Qt
from widgets.custom_widgets import SecondPanel, DarkInput, DarkButton
from settings.languages import lang_manager
from settings.values import CYLINDER_VALUES, GRAPH_SIGNAL
from calculator import CylFormula
from .cylinder_graph import CylinderGraph
from PySide6.QtWidgets import (
    QVBoxLayout,
    QGridLayout,
    QLabel,
)


class Cylinder(SecondPanel):
    def __init__(self):
        super().__init__()


        # Input Boxes
        self.boreInput = DarkInput()
        self.rodInput = DarkInput()
        self.pressureInput = DarkInput()


        # Labels
        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(
            """
            font-size: 20px;
            font-weight: bold;
            padding: 6px;
            """
        )

        self.output = QLabel()
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setMinimumHeight(40)

        # Buttons
        self.calcButton = DarkButton()
        self.resetButton = DarkButton()

        self.graph = CylinderGraph()

        
        # Button layout
        buttonLayout = QGridLayout()
        buttonLayout.addWidget(self.calcButton, 0, 0)
        buttonLayout.addWidget(self.resetButton, 0, 1)
        
        # Main screen layout
        mainLayout = QVBoxLayout()

        inputLayout = QVBoxLayout()
        inputLayout.addWidget(self.title)
        inputLayout.addWidget(self.boreInput)
        inputLayout.addWidget(self.rodInput)
        inputLayout.addWidget(self.pressureInput)
        inputLayout.addWidget(self.output)
        inputLayout.addLayout(buttonLayout)

        graphLayout = QVBoxLayout()
        graphLayout.addWidget(self.graph)

        mainLayout.addLayout(inputLayout, 40)
        mainLayout.addLayout(graphLayout, 60)

        self.setLayout(mainLayout)

        self.calcButton.clicked.connect(self.calculate)
        self.resetButton.clicked.connect(self.reset)

        self.push = 0
        self.pull = 0

        self.current_error = None


        self.updateOutputs()
        self.updateLanguage()


        lang_manager.language_changed.connect(
            self.updateLanguage
        )
        lang_manager.language_changed.connect(
            self.updateOutputs
        )

    def calculate(self):        
        try:
            bore = float(self.boreInput.text())
            rod = float(self.rodInput.text())
            pressure = float(self.pressureInput.text())

            if rod < 0 or bore < 0 or pressure < 0:
                self.current_error = 'negative_error'
                self.updateOutputs()
                return
                
            if rod >= bore:
                self.current_error = 'rod_bore_error'
                self.updateOutputs()
                return
                
            calc = CylFormula(
                bore=bore,
                rod=rod,
                pressure=pressure
            )

            self.push = calc.cyl_ext_force()
            self.pull = calc.cyl_ret_force()

            CYLINDER_VALUES['bore'] = bore
            CYLINDER_VALUES['rod'] = rod
            CYLINDER_VALUES['pressure'] = pressure
            CYLINDER_VALUES['push_force'] = self.push
            CYLINDER_VALUES['pull_force'] = self.pull

            GRAPH_SIGNAL.force_changed.emit(self.push)

            self.current_error = None

            self.updateOutputs()

            
        except ValueError:
            self.current_error = 'invalid_input'
            self.updateOutputs()

        print(CYLINDER_VALUES)

    def reset(self):
        self.boreInput.clear()
        self.rodInput.clear()
        self.pressureInput.clear()

        self.push = 0
        self.pull = 0
        self.current_error = None

        self.updateLanguage()
        self.updateOutputs()

    def updateOutputs(self):

        if self.current_error:
            self.output.setText(
                lang_manager.get_text(
                    self.current_error
                    )
            )
            return
        
        self.output.setText(
            f"{lang_manager.get_text('push_force')} {self.push:,.0f} "
            f" {lang_manager.get_text('pounds')}\n"
            f"{lang_manager.get_text('pull_force')} {self.pull:,.0f} "
            f" {lang_manager.get_text('pounds')}"
        )



    def updateLanguage(self):

        self.title.setText(
            lang_manager.get_text('cylinder')
        )
        self.calcButton.setText(
            lang_manager.get_text('calculate')
        )
        self.resetButton.setText(
            lang_manager.get_text('reset')
        )
        self.boreInput.setPlaceholderText(
            lang_manager.get_text('bore_hint')
        )
        self.rodInput.setPlaceholderText(
            lang_manager.get_text('rod_hint')
        )
        self.pressureInput.setPlaceholderText(
            lang_manager.get_text('pressure_hint')
        )
















