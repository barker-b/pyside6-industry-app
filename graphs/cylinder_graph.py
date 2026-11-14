import math
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import pyqtgraph as pg
from widgets.custom_widgets import SecondPanel, ThemedInput, ThemedButton
from settings.languages import lang_manager
from settings.values import CYLINDER_VALUES, GRAPH_SIGNAL
from PySide6.QtWidgets import (
    QVBoxLayout,
    QGridLayout,
    QLabel,
)


class CylinderGraph(SecondPanel):
        def __init__(self):
            super().__init__()

            self.cyl_graph = pg.PlotWidget()
            self.cyl_graph.setTitle('angle_force', size='15pt')


            self.graphFont = QFont()
            self.graphFont.setPointSize(15)

            self.x_axis = self.cyl_graph.getAxis('bottom')
            self.x_axis.setLabel('graph_angle')
            self.x_axis.setTickSpacing(10, 10)
            self.x_axis.label.setFont(self.graphFont)

            self.y_axis = self.cyl_graph.getAxis('left')
            self.y_axis.setTickSpacing(2000, 2000)
            self.y_axis.setLabel('graph_force')
            self.y_axis.label.setFont(self.graphFont)

            self.cyl_graph.addLegend()

            self.push_force = CYLINDER_VALUES['push_force']
            self.pull_force = CYLINDER_VALUES['pull_force']
          

            layout = QVBoxLayout()
            layout.addWidget(self.cyl_graph)

            self.setLayout(layout)

            GRAPH_SIGNAL.force_changed.connect(self.update_graph)

            self.update_graph(self.push_force, self.pull_force,)
            
            self.updateLanguage()

            lang_manager.language_changed.connect(
                self.updateLanguage
            )



        def update_graph(self, new_push_force, new_pull_force):
            self.push_force = new_push_force
            self.pull_force = new_pull_force
            self.cyl_graph.clear()
            print('so far so good')

            if new_push_force == 0:
                self.cyl_graph.setXRange(0, 91)
                self.cyl_graph.setYRange(0, 10000)
                return

            x_push = []
            y_push = []
            x_pull = []
            y_pull = []

            for angle in range(10, 91, 10):
                angle_force = new_push_force * math.sin(
                    math.radians(angle)
                )
                y_push.append(angle_force)
                x_push.append(angle)

            for angle in range(10, 91, 10):
                angle_force = new_pull_force * math.sin(
                    math.radians(angle)
                )
                y_pull.append(angle_force)
                x_pull.append(angle)

            self.cyl_graph.showGrid(x=True, y=True)
            self.cyl_graph.setYRange(0, new_push_force,)
            self.cyl_graph.setXRange(0, 91)
            self.push_line = self.cyl_graph.plot(
                x_push,
                y_push,
                name=lang_manager.get_text('push_force'),
                pen='r'
                )
            self.pull_line = self.cyl_graph.plot(
                x_pull,
                y_pull,
                name=lang_manager.get_text('pull_force'),
                pen='b'
                )

            print(x_push)
            print(y_push)


        def updateLanguage(self):
            self.cyl_graph.setTitle(
                 lang_manager.get_text(
                      'angle_force'
                 )
            )
            self.y_axis.setLabel(
                 lang_manager.get_text(
                      'graph_force'
                 )
            )
            self.x_axis.setLabel(
                 lang_manager.get_text(
                      'graph_angle'
                 )
            )



