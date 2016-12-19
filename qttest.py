from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
#from utils import *
import sip
import sys


class MyWizard(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # vertical layout, wraps content layout and buttons layout
        vertical_layout = QtWidgets.QVBoxLayout()
        self.setLayout(vertical_layout)

        # content widget and layout
        self.content_layout = QtWidgets.QVBoxLayout()  # could be almost any layout actually
        self.content = QtWidgets.QLabel('PrivaSee에 오신것을 환영합니다.\n 당신의 이름을 영어로 적어주세요^^')  # customize with your content
        self.content_layout.addWidget(self.content)
        vertical_layout.addLayout(self.content_layout)
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 200)
        self.textbox.resize(200, 40)

        # back, forward buttons wraped in horizontal layout
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addStretch()
        self.forward_button = QtWidgets.QPushButton('다음')
        self.forward_button1 = QtWidgets.QPushButton('다음')
        self.forward_button2 = QtWidgets.QPushButton('다음')
        self.forward_button3 = QtWidgets.QPushButton('다음')
        self.forward_button4 = QtWidgets.QPushButton('다음')
        self.forward_button5 = QtWidgets.QPushButton('다음')
        self.forward_button.clicked.connect(self.forward_button_clicked)
        self.button_layout.addWidget(self.forward_button)
        self.vertical_layout.addLayout(self.button_layout)

    def forward_button_clicked(self):
        textboxValue = self.textbox.text()
        with open('name.txt', 'w') as f:
            f.write(textboxValue)
            f.close()

        # remove old content
        sip.delete(self.textbox)
        sip.delete(self.forward_button)
        self.content_layout.removeWidget(self.content)
        self.content.deleteLater()

        # create new content
        self.content = QtWidgets.QLabel('')

        # add new content
        self.content_layout.addWidget(self.content)


app = QtWidgets.QApplication([])

wizard = MyWizard()
wizard.setWindowTitle('PrivaSee tutorial')
wizard.setFixedSize(600, 400)
wizard.show()

app.exec_()
