import math
from PySide6.QtCore import Qt
import pyqtgraph as pg
from widgets.custom_widgets import SecondPanel, DarkInput, DarkButton
from settings.languages import lang_manager
from settings.values import CYLINDER_VALUES, GRAPH_SIGNAL
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

            layout = QVBoxLayout()
            layout.addWidget(self.cyl_graph)

            self.setLayout(layout)

            GRAPH_SIGNAL.force_changed.connect(self.update_graph)

            self.update_graph(self.push_force)

        def update_graph(self, new_force):
            self.push_force = new_force

            x = []
            y = []

            for angle in range(10, 91, 10):
                angle_force = new_force * math.sin(
                        math.radians((angle))
                        )
                y.append(angle_force)
                x.append(angle)


            self.line = self.cyl_graph.plot(x, y)
            self.line.setData(x, y)

            print(x)
            print(y)


