from views.FrmEncriptar import *

class Encriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.btnEncriptar.clicked.connect(self.encriptarAES)

    def encriptarAES(self):
        data = self.txtMensaje.toPlainText()
        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024IGDS"
        print(data)