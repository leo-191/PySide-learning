import sys

from PySide6.QtWidgets import QApplication, QWidget

# sys.argv 用于给应用提供命令行
app = QApplication((sys.argv))

window = QWidget()
window.show()  # window 默认不显示

# 事件循环
app.exec()


# 此处的代码块永远不会被触发，直至退出事件循环
