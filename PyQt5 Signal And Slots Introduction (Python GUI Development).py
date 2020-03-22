from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Event And Signals"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 320
        self.iconName = 'Images/home-icon.png'

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateButton()

        self.show()

    
    def CreateButton(self):
        #Button Components Click me
        button = QPushButton("Click Me", self)
        button.setGeometry(QRect(100, 100, 111, 50))
        button.setIcon(QtGui.QIcon('Images/home-icon.png'))
        button.setIconSize(QtCore.QSize(40,40))
        button.clicked.connect(self.ClickMe)

        #Button Components exit
        button = QPushButton("Exit", self)
        button.setGeometry(QRect(250, 220, 100, 70))
        button.setIcon(QtGui.QIcon('Images/home-icon.png'))
        button.setIconSize(QtCore.QSize(40,40))
        button.clicked.connect(self.Exit)



    def ClickMe(self):
        #This part is displayed in the terminal.
        print("Your Clicked")


    def Exit(self):
        sys.exit()




if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

    

