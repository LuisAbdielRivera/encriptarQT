from views.FrmDesencriptar import *
from views.FrmEncriptar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import *


class Desencriptar(QtWidgets.QMainWindow, Ui_FrmDesencriptar):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.btnDesencriptar.clicked.connect(self.desencriptarAES)
        self.btnCargarArchivo.clicked.connect(self.cargarArchivo)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)

    def cargarArchivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*.txt);; Python Files (*.py)", options = options)
        if fileName:
            with open(fileName, 'r') as fichero:
                mensaje = fichero.read()
            self.lblMensajeEncriptado.setText(mensaje)

    def limpiarCampos(self):
        self.lblMensajeEncriptado.clear()
        self.lblMensajeEncriptado_2.clear()

    def desencriptarAES(self):
        data = self.lblMensajeEncriptado.text()
        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"
        cadena_bytes = eval(data)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
        descryptor = cipher.decryptor()
        mensaje_desencriptado = descryptor.update(cadena_bytes) + descryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        mensaje_desencriptado = unpadder.update(mensaje_desencriptado) + unpadder.finalize()
        self.lblMensajeEncriptado_2.setText(mensaje_desencriptado.decode('utf-8'))

        print(data)