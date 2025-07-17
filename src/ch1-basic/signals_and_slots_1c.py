import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 在父类中保存 button 状态信息
        self.button_is_checked = True
        self.setWindowTitle("My APP")

        button = QPushButton("Press Me!")
        button.setCheckable(True)

        button.clicked.connect(self.the_button_was_toggled)

        # 更新 button 的状态信息
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
