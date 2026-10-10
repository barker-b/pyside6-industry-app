DARK_THEME = """

QMainWindow {
    background-color: #1E1E1E;
    }

QWidget#central {
    background-color: #1E1E1E;
    }

BasePanel {
    border: 2px solid #B3B4BA;
    background-color: #1E1E1E;
    border-radius: 6px;
    padding: 12px;
}

SecondPanel {
    border: .5px solid #B3B4BA;
    background-color: #2A2A2A;
    border-radius: 6px;
}
DarkInput { background-color: #1E1E1E;
}

DarkButton { background-color: #1E1E1E;
}

* {
    color: #E0E0E0;
    }
"""

LILGHT_THEME = """
BasePanel {
    border: 2px solid #2A2A2A;
    border-radius: 6px;
    padding: 12px;
}

SecondPanel {
    background-color: #FFFFFF;
    border: .5px solid #2A2A2A;
    border-radius: 12px;
    }
"""
THEMES = {
    "light": LILGHT_THEME,
    "dark": DARK_THEME
}