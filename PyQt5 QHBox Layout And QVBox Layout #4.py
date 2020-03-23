from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layout Management"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.iconName = 'home-icon.png'

        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)
        
        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Game ?")

        hboxlayout = QHBoxLayout()

        button = QPushButton("Pes2020",self)
        button.setIcon(QtGui.QIcon('Images/pes2020.jpeg'))
        button.setIconSize(QtCore.QSize(50,100))
        button.setMinimumHeight(100)
        hboxlayout.addWidget(button)

        
        button1 = QPushButton("PUBG",self)
        button1.setIcon(QtGui.QIcon('Images/pubg.jpeg'))
        button1.setIconSize(QtCore.QSize(50,100))
        button1.setMinimumHeight(100)
        hboxlayout.addWidget(button1)

        
        button2 = QPushButton("Call of duty",self)
        button2.setIcon(QtGui.QIcon('Images/callofduty.png'))
        button2.setIconSize(QtCore.QSize(100,100))
        button2.setMinimumHeight(100)
        hboxlayout.addWidget(button2)
        
        self.groupBox.setLayout(hboxlayout)
        

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
