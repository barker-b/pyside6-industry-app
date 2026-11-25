import math
from PySide6.QtGui import QFont
import pyqtgraph as pg
from widgets.custom_widgets import SecondPanel
from settings.languages import lang_manager
from settings.values import MOTOR_VALUES, GRAPH_SIGNAL
from PySide6.QtWidgets import QVBoxLayout

class MotorGraph(SecondPanel):
    def __init__(self):
        super().__init__()

        self.mot_graph = pg.PlotWidget()
        self.mot_graph.setTitle("Motor")

        layout = QVBoxLayout()
        layout.addWidget(self.mot_graph)

        self.setLayout(layout)