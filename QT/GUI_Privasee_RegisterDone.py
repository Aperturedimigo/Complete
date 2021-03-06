import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

windowSizeX = 440
windowSizeY = 250

fontMajor = "Arial"
fontMinor = "Dotum"

class Form(QWidget):
    # __init__ : 생성자
    # parent : 부모객체
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        nameLabel = QLabel()
        nameLabel.setText("Register Successfully Done!")
        newfont = QtGui.QFont(fontMinor, 16, QtGui.QFont.Bold)
        nameLabel.setFont(newfont)
        nameLabel.setAlignment(Qt.AlignCenter)

        blankLabel = QLabel()
        blankLabel.setText(" ")

        mainButton = QPushButton("Go Main")

        mainButton.clicked.connect(self.mainContact)

        mainLayout = QGridLayout()

        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(mainButton,1,0)

        self.setLayout(mainLayout)

        self.setWindowTitle("Privasee")

    def mainContact(self):
        '''call GUI_Privasee_Main.py'''
        sys.exit(app.exec_())

if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = Form()
    screen.resize(windowSizeX,windowSizeY)
    screen.show()

    sys.exit(app.exec_())
