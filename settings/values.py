from PySide6.QtCore import QObject, Signal

class GraphSignals(QObject):
    force_changed = Signal(float)

GRAPH_SIGNAL = GraphSignals()

# Store Values from inputs

CYLINDER_VALUES = {
    'bore': 0,
    'rod': 0,
    'pressure': 0,
    'push_force': 0,
    'pull_force': 0,

}

MOTOR_VALUES = {
    'displacement': 0,
    'flow': 0,
    'pressure': 0,
    'motor_torque': 0,
    'motor_speeed': 0,

}

PUMP_VALUES = {
    'displacement': 0,
    'speed': 0,
    'pressure': 0,
    'pump_flow': 0,
    'horse_power': 0,
    'required_torque': 0, 

}