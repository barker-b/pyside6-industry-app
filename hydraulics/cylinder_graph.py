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

            self.x_axis = self.cyl_graph.getAxis('bottom')
            self.x_axis.setLabel('Anlge')
            self.x_axis.setTickSpacing(10, 10)

            self.y_axis = self.cyl_graph.getAxis('left')
            self.y_axis.setTickSpacing(2000, 2000)
            self.y_axis.setLabel('Force (lbs)')


            self.push_force = CYLINDER_VALUES['push_force']

            layout = QVBoxLayout()
            layout.addWidget(self.cyl_graph)

            self.setLayout(layout)

            GRAPH_SIGNAL.force_changed.connect(self.update_graph)

            self.update_graph(self.push_force)

        def update_graph(self, new_force):
            self.push_force = new_force
            self.cyl_graph.clear()

            if new_force == 0:
                self.cyl_graph.setXRange(0, 91)
                self.cyl_graph.setYRange(0, 10000)
                return

            x = []
            y = []

            for angle in range(10, 91, 10):
                angle_force = new_force * math.sin(
                        math.radians(angle)
                        )
                y.append(angle_force)
                x.append(angle)


            self.cyl_graph.showGrid(x=True, y=True)
            self.cyl_graph.setYRange(0, new_force,)
            self.cyl_graph.setXRange(0, 91)
            self.line = self.cyl_graph.plot(x, y)

            print(x)
            print(y)


