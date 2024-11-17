from views.FrmMenu import *
from Encriptar import *
from Desencriptar import *

class Menu(QtWidgets.QMainWindow, Ui_FrmMenu):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.btnEncriptar.clicked.connect(self.openEncriptar)
        self.btnDesencriptar.clicked.connect(self.openDesencriptar)

    def openEncriptar(self):
        opennewwindow = Encriptar(self)
        opennewwindow.show()

    def openDesencriptar(self):
        opennewwindow = Desencriptar(self)
        opennewwindow.show()