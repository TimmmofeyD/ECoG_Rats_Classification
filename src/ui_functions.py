from Custom_Widgets import *
from PySide6.QtCore import QSettings, QTimer

class GuiFunctions():
    def __init__(self, MainWindow):
        self.main = MainWindow
        self.ui = MainWindow.ui

        self.initializeTheme()

    def initializeTheme(self):
        settings = QSettings()
        current_theme = settings.value("THEME")