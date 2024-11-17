from views.FrmDesencriptar import *

class Desencriptar(QtWidgets.QMainWindow, Ui_FrmDesencriptar):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)
