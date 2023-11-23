import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('Ui.ui', self)
        self.btn.clicked.connect(self.paint_okr)

    def paint_okr(self):
        self.update()

    def paintEvent(self, event):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(a, b, c))
        qp.setBrush(QColor(a, b ,c))
        x = random.randint(10, 300)
        y = random.randint(10, 300)
        size = random.randint(20, 200)
        qp.drawEllipse(x, y, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
