import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 更改应用标题
        self.setWindowTitle("My APP")
        button = QPushButton("Press Me!")

        # 将一个 widget 放入到当前 window 中，居中
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
