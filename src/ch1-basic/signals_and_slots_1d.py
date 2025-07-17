import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 在父类中保存 button 状态信息
        self.button_is_checked = True
        self.setWindowTitle("My APP")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        # released 也是 button 的内置信号，在 button 释放时触发，但不具任何额外数据
        self.button.released.connect(self.the_button_was_released)

        # 更新 button 的状态信息
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        # 通过类成员变量传递数据
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
