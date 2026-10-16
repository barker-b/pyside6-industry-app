# Language dictionarires

SPANISH = {
    'greeting': 'Hola Mundo',
    'hydraulics': 'Hidráulica',
    'cylinder': 'Cilindro',
    'motor': 'Motor',
    'pump': 'Bomba',
}

ENGLISH = {
    'greeting': 'Hello World',
    'hydraulics': 'Hydraulics',
    'cylinder': 'Cylinder',
    'motor': 'Motor',
    'pump': 'Pump',
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