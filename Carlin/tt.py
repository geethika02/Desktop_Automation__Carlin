from gui2 import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import sample

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        sample.security()

startfunctions = MainThread()


class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)

    def startfun(self):
        self.jarvis_ui.movies_2 = QtGui.QMovie("GUI/__1.gif")
        self.jarvis_ui.sm.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_3 = QtGui.QMovie("GUI/Jarvis_Gui (1).gif")
        self.jarvis_ui.middle.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("GUI/Earth.gif")
        self.jarvis_ui.earth.setMovie(self.jarvis_ui.movies_4)
        self.jarvis_ui.movies_4.start()

        self.jarvis_ui.movies_5 = QtGui.QMovie("GUI/dribbble.gif")
        self.jarvis_ui.percent.setMovie(self.jarvis_ui.movies_5)
        self.jarvis_ui.movies_5.start()

        self.jarvis_ui.movies_6 = QtGui.QMovie("GUI/200.gif")
        self.jarvis_ui.code.setMovie(self.jarvis_ui.movies_6)
        self.jarvis_ui.movies_6.start()

        self.jarvis_ui.movies_7 = QtGui.QMovie("GUI/0baf79ba59be86610edc1f810a79f2b7.gif")
        self.jarvis_ui.loadpic.setMovie(self.jarvis_ui.movies_7)
        self.jarvis_ui.movies_7.start()

        self.jarvis_ui.movies_8 = QtGui.QMovie("GUI/initial.gif")
        self.jarvis_ui.initialize.setMovie(self.jarvis_ui.movies_8)
        self.jarvis_ui.movies_8.start()

        startfunctions.start()



gui_app = QApplication(sys.argv)
gui_jarvis = Gui_start()
gui_jarvis.startfun()
gui_jarvis.show()
exit(gui_app.exec_())