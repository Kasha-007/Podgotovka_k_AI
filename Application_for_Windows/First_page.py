# Hi, my name is Yasha and this is my first English project
# import PyQt5
# Make changes in browser
# Check changes in Pycharm 2
# Ok, changes are visible
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, QRect


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def load_txt(self):
        k = open('Hi, Yasha')
        with k:
            k2 = k.read()
            self.qle.setText(k2)
            self.setText_btn.setText(k2)

    def set_txt(self):
        k = open('Hi, Yasha', 'w+')
        self.loadText_btn.setText(self.qle.text())
        with k:
            k.write(self.qle.text())

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200, 250)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Quit button')
        self.setWindowIcon(QIcon('web.png'))

        self.qle = QLineEdit(self)
        self.qle.move(60, 100)
        self.qle.setText('Hi')

        self.setText_btn = QPushButton('Hi', self)
        self.setText_btn.clicked.connect(self.load_txt)
        self.setText_btn.resize(60, 25)
        self.setText_btn.move(60, 140)

        self.loadText_btn = QPushButton('', self)
        self.loadText_btn.clicked.connect(self.set_txt)
        self.loadText_btn.resize(60, 25)
        self.loadText_btn.move(130, 140)

        self.show()
        k = open('Hi, Yasha', 'w')
        with k:
            return k.write('Hi')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
