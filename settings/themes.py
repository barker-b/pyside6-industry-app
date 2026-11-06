DARK_THEME = """

QMainWindow {
    background-color: #2A2A2A;
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
ThemedInput { background-color: #1E1E1E;
}

ThemedButton { background-color: #1E1E1E;
}

* {
    color: #E0E0E0;
    }
"""

LIGHT_THEME = """

QMainWindow {
    background-color: #FFFFFF;
    }

BasePanel {
    background-color: #F3F3F3;
    border: 2px solid #2A2A2A;
    border-radius: 6px;
    padding: 12px;
}

SecondPanel {
    background-color: #FFFFFF;
    border: .5px solid #2A2A2A;
    border-radius: 12px;
    }
ThemedButton { background-color: #F3F3F3;
}

ThemedInput { background-color: #F3F3F3;
}

* {
    color: #000000;
    }
"""
BLUE_THEME = """
"""

THEMES = {
    "light": LIGHT_THEME,
    "dark": DARK_THEME,
    "blue": BLUE_THEME,
}