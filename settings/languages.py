# Language dictionarires

SPANISH = {
    'greeting': 'Hola Mundo',
    'hydraulics_feminine': 'Hidráulica',
    'hydraulic_motor': 'Motor\nHidráulico',
    'cylinder': 'Cilindro',
    'motor': 'Motor',
    'pump': 'Bomba',
    'coming_soon': 'Sección en desarrollo',
    'electrical': 'Eléctrica',
    'electrical_motor': 'Motor\nEléctrico',
    'calculate': 'Calcular',
    'reset': 'Restablecer',
    'pounds': 'Libras',
    'push_force': 'Fuerza de empuje',
    'pull_force': 'Fuerza de tracción',
    'motor_torque': 'Torque del Motor',
    'motor_speed': 'Velocidad del Motor',
    'pump_flow': 'Caudal de la Bomba',
    'horse_power': 'Potencia de la Bomba',
    'required_torque': 'Torque Requerido',    
    'bore_hint': 'Diámetro interior (pulg.)',
    'rod_hint': 'Diámetro de Barra (pulg.)',
    'pressure_hint': 'Presión (PSI)',
    'displacement_hint': 'Desplazamiento (CIR)',
    'flow_hint': 'Caudal (GPM)',
    'speed_hint': 'Velocidad (RPM)',
    'rod_bore_error': 'Inválido, la barra no puede ser\n'
                      'igual o más grande que el diámetro.',
    'negative_error': 'Inválido, los valores deben ser\n'
                      'números positivos.',
    'invalid_input': 'Por favor ingrese números válidos.',


}

ENGLISH = {
    'greeting': 'Hello World',
    'hydraulics': 'Hydraulics',
    'hydraulic_motor': 'Hydraulics\nMotor',
    'hydraulic': 'Hydraulic',
    'cylinder': 'Cylinder',
    'motor': 'Motor',
    'pump': 'Pump', 
    'coming_soon': 'Coming Soon',
    'electrical': 'Electrical',
    'electrical_motor': 'Electrical\nMotor',
    'calculate': 'Calculate',
    'reset': 'Reset',
    'pounds': 'Pounds',
    'push_force': 'Push force',
    'pull_force': 'Pull force',
    'motor_torque': 'Motor Torque',
    'motor_speed': 'Motor Speed',
    'pump_flow': 'Pump Flow',
    'horse_power': 'Horsepower',
    'required_torque': 'Required Torque',     
    'bore_hint': 'Bore Diameter (in)',
    'rod_hint': 'Rod Diameter (in)',
    'pressure_hint': 'Pressure (PSI)',
    'displacement_hint': 'Displacement (in³)',
    'flow_hint': 'Flow (GPM)',
    'speed_hint': 'Speed (RPM)',
    'rod_bore_error': 'Invalid, rod cannot be\n'
                      'the same or larger than bore.',
    'negative_error': 'Invalid, inputs must be\n'
                      'positive numbers.',
    'invalid_input': 'Please enter valid numbers.',
}


LANGUAGE = {
    'es': SPANISH,
    'en': ENGLISH,
}

from PySide6.QtCore import QObject, Signal

class LanguageManager(QObject):


    language_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_language = "en"
        self.strings = LANGUAGE

    def set_language(self, lang_code):
        if lang_code in self.strings:
            self.current_language = lang_code
            self.language_changed.emit(lang_code)

    def get_text(self, key):
        lang_dict = self.strings.get(self.current_language, self.strings["en"])
        return lang_dict.get(key, key)

lang_manager = LanguageManager()