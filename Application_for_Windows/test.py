import sys

from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                     "Nullam malesuada tellus in ex elementum, vitae rutrum "
                     "enim vestibulum.")

        self.label = QtWidgets.QLabel(self.text)
        self.label.setWordWrap(True)

        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

        self.show()


app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
