from PySide6.QtCore import Qt
import pyqtgraph as pg
from widgets.custom_widgets import SecondPanel, DarkInput, DarkButton
from settings.languages import lang_manager
from settings.values import CYLINDER_VALUES
from calculator import CylFormula
from PySide6.QtWidgets import (
    QVBoxLayout,
    QGridLayout,
    QLabel,
)


class CylinderGraph(SecondPanel):
        def __init__(self):
            super().__init__()

            self.cyl_graph = pg.PlotWidget()
            self.cyl_graph.setTitle("Force at angles")
            self.cyl_graph.setLabel('left', 'Angle')
            self.cyl_graph.setLabel('bottom', 'Push Force')

            self.push_force = CYLINDER_VALUES['push_force']

            x = []
            y = []

            self.cyl_graph.plot(x, y)

            layout = QVBoxLayout()
            layout.addWidget(self.cyl_graph)

            self.setLayout(layout)


