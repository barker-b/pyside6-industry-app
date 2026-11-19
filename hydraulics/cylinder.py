from PySide6.QtCore import Qt
from widgets.custom_widgets import SecondPanel, ThemedInput, ThemedButton
from settings.languages import lang_manager
from settings.values import CYLINDER_VALUES, GRAPH_SIGNAL
from calculator import CylFormula
from graphs.cylinder_graph import CylinderGraph
from PySide6.QtWidgets import (
    QVBoxLayout,
    QGridLayout,
    QLabel,
)


class Cylinder(SecondPanel):
    def __init__(self):
        super().__init__()


        # Input Boxes
        self.boreInput = ThemedInput()
        self.rodInput = ThemedInput()
        self.pressureInput = ThemedInput()


        # Labels
        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(
            """
            font-size: 30px;
            font-weight: bold;
            padding: 15px;
            """
        )

        self.output = QLabel()
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setMinimumHeight(40)
        self.output.setStyleSheet(
            """
            font-size: 20px;
            """
        )
        
        # Inputs
        inputLayout = QVBoxLayout()
        inputLayout.setContentsMargins(50, 0, 50, 0)
        inputLayout.addWidget(self.boreInput)
        inputLayout.addWidget(self.rodInput)
        inputLayout.addWidget(self.pressureInput)
        inputLayout.addWidget(self.output)

        # Buttons
        self.calcButton = ThemedButton()
        self.resetButton = ThemedButton()
        
        # Button layout
        buttonLayout = QGridLayout()
        buttonLayout.setContentsMargins(25, 0, 25, 0)
        buttonLayout.addWidget(self.calcButton, 0, 0)
        buttonLayout.addWidget(self.resetButton, 0, 1)


        # Graph
        self.graph = CylinderGraph()
        graphLayout = QVBoxLayout()
        graphLayout.addWidget(self.graph)

        # Main screen layout
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.title, 10)
        mainLayout.addLayout(inputLayout, 20)
        mainLayout.addLayout(buttonLayout, 10)
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

            GRAPH_SIGNAL.force_changed.emit(self.push, self.pull)


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

        GRAPH_SIGNAL.force_changed.emit(self.push, self.pull)

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
            f"{lang_manager.get_text('push_force')} {self.push:,.0f}"
            f" {lang_manager.get_text('pounds')}\n"
            f"{lang_manager.get_text('pull_force')} {self.pull:,.0f}"
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
















