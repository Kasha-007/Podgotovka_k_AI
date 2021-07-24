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

        setText_btn = QPushButton('Hi', self)
        setText_btn.clicked.connect(lambda x: self.qle.setText('Hi'))
        setText_btn.resize(60, 25)
        setText_btn.move(60, 140)

        loadText_btn = QPushButton('', self)
        loadText_btn.clicked.connect(lambda x: loadText_btn.setText(self.qle.text()))
        loadText_btn.resize(60, 25)
        loadText_btn.move(130, 140)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
