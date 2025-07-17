import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My APP")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        # clicked 是 button widget 的内置信号
        # 将 clicked 与 the_button_was_clicked 连接
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        """button widget clicked signal 的 slot"""
        print("Clicked!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
