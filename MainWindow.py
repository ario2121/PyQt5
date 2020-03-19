from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtGui  


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Main Window"
        self.top = 300
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = 'home-icon.png'


        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
