import sys

from layout_colorwidget import Color
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        tabs = QTabWidget()
        # macOS 样式兼容
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)
        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
