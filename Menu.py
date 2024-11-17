from views.FrmMenu import *
from Encriptar import *
from Desencriptar import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Menu(QtWidgets.QMainWindow, Ui_FrmMenu):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.encriptarNuevo.triggered.connect(self.openEncriptar)
        self.desencriptarNuevo.triggered.connect(self.openDesencriptar)

    def openEncriptar(self):
        opennewwindow = Encriptar(self)
        opennewwindow.show()

    def openDesencriptar(self):
        opennewwindow = Desencriptar(self)
        opennewwindow.show()