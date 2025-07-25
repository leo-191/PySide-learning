import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("This is a checkbox")
        widget.setCheckState(Qt.CheckState.Checked)

        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()