import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QFrame,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)

from calculator import CylFormula


class Cylinder(QFrame):
    def __init__(self):
        super().__init__()

        # Panel design
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("cylinderPanel")
        self.setStyleSheet("""
            #cylinderPanel {
                border: 1px solid #2A2A2A;
                border-radius: 6px;
                background-color: #ffffff
            }
        """)


        # Input Boxes
        self.boreInput = QLineEdit()
        self.boreInput.setPlaceholderText("Bore Size (in)")
        self.boreInput.setStyleSheet("""
            QLineEdit {
                qproperty-alignment: AlignCenter;
            }
        """)



        self.rodInput = QLineEdit()
        self.rodInput.setPlaceholderText("Rod Size (in)")

        self.pressureInput = QLineEdit()
        self.pressureInput.setPlaceholderText("Pressure (psi)")

        # Labels
        self.title = QLabel("Cylinder")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                padding: 6px;
                }
        """)

        self.output = QLabel("Push Force: 0 \nPull Force: 0 ")
        self.output.setAlignment(Qt.AlignCenter)

        # Buttons
        self.calcButton = QPushButton("Calculate")
        self.resetButton = QPushButton("Reset")


        # Button layout
        buttonLayout = QGridLayout()
        buttonLayout.addWidget(self.calcButton, 0, 0)
        buttonLayout.addWidget(self.resetButton, 0, 1)
        
        # Main screen layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title)
        mainLayout.addWidget(self.boreInput)
        mainLayout.addWidget(self.rodInput)
        mainLayout.addWidget(self.pressureInput)
        mainLayout.addWidget(self.output)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)

        self.calcButton.clicked.connect(self.calculate)
        self.resetButton.clicked.connect(self.reset)

    def calculate(self):
        try:
            bore = float(self.boreInput.text())
            rod = float(self.rodInput.text())
            pressure = float(self.pressureInput.text())

            calc = CylFormula(
                bore=bore,
                rod=rod,
                pressure=pressure
            )

            push = calc.cyl_ext_force()
            pull = calc.cyl_ret_force()

            self.output.setText(
                f"Push Force: {push:,.0f} pounds.\n"
                f"Pull Force: {pull:,.0f} pounds."
            )
            
        except ValueError:
            self.output.setText("error")

    def reset(self):
        self.output.setText("Push Force: 0 \nPull Force: 0")




