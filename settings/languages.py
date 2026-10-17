# Language dictionarires

SPANISH = {
    'greeting': 'Hola Mundo',
    'fem hydraulics': 'Hidráulica',
    'mas hydraulics': 'Hidraulico',
    'cylinder': 'Cilindro',
    'motor': 'Motor',
    'pump': 'Bomba',
    'coming soon': 'Sección en desarrollo',
    'electric': 'Eléctrica',
}

ENGLISH = {
    'greeting': 'Hello World',
    'fem hydraulics': 'Hydraulics',
    'mas hydraulics': 'Hydraulics',
    'hydraulic': 'Hydraulic',
    'cylinder': 'Cylinder',
    'motor': 'Motor',
    'pump': 'Pump',
    'coming soon': 'Coming soon',
    'electrical': 'Electrical'
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