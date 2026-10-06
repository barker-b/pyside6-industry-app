import sys
from cylinder import Cylinder
from motors import Motor
from pump import Pump
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QGridLayout,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indusrty Calculator")
        self.resize(800, 800)

        # Tool bar
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Layout
        layout = QGridLayout()
        central_widget.setLayout(layout)


        # Placeholders for now
        electricLabel = QLabel("Coming Soon!")
        fluidsLabel = QLabel("Coming Soon!")
        materialsLabel = QLabel("Coming Soon!")
        extraPanel = QLabel("Coming soon!")
        extraPanel.setAlignment(Qt.AlignCenter)
    
        # hydraulic imports
        cylPanel = Cylinder()
        motorPanel = Motor()
        pumpPanel = Pump()


        # top level panels
        hydraulicsPanel = QGridLayout()
        hydraulicsPanel.addWidget(cylPanel, 0, 0)
        hydraulicsPanel.addWidget(motorPanel, 0 , 1)
        hydraulicsPanel.addWidget(pumpPanel, 1, 0)
        hydraulicsPanel.addWidget(extraPanel, 1, 1)


        hydraulicsPanel.setColumnStretch(1, 1)

        electricPanel = QGridLayout()
        electricPanel.addWidget(electricLabel)
        electricLabel.setAlignment(Qt.AlignCenter)

        fluidsPanel = QGridLayout()
        fluidsPanel.addWidget(fluidsLabel)
        fluidsLabel.setAlignment(Qt.AlignCenter)

        materialsPanel = QGridLayout()
        materialsPanel.addWidget(materialsLabel)
        materialsLabel.setAlignment(Qt.AlignCenter)

        layout.addLayout(hydraulicsPanel, 0, 0)
        layout.addLayout(electricPanel, 0, 1)
        layout.addLayout(fluidsPanel, 1, 0)
        layout.addLayout(materialsPanel, 1, 1)

        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)


        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())