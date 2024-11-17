from views.FrmMenu import *

class Menu(QtWidgets.QMainWindow, Ui_FrmMenu):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)