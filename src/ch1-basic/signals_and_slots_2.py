import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My APP")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        # 点击一点后切换文本并禁用 button
        self.button.setText("You already clicked me,")
        self.button.setEnabled(False)

        # 也可在 handler 中做其他操作
        self.setWindowTitle("My Oneshot APP")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
