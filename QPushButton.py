from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "QPushButton"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 320
        self.UiComponents()
        self.InitWindow()
        

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('home-icon.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def UiComponents(self):
        button = QPushButton("Click me",self)
        button.setGeometry(QRect(100,100,101,50))
        
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
