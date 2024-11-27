#pip install cryptography
from views.FrmEncriptar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import *

class Encriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.btnEncriptar.clicked.connect(self.encriptarAES)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)
        self.btnGuardarArchivo.clicked.connect(self.crearArchivos)
        self.btnCargarArchivo.clicked.connect(self.cargarArchivo)

    def encriptarAES(self):
        data = self.txtMensaje.toPlainText()
        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode('utf-8'))
        padded_data += padder.finalize()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data)+encryptor.finalize()
        self.lblMensajeEncriptado.setText(f'{ciphertext}')
        print(data)

    def limpiarCampos(self):
        self.lblMensajeEncriptado.clear()
        self.txtMensaje.clear()

    def crearArchivos(self):
        cadena = self.lblMensajeEncriptado.text()
        if cadena != "":
            fecha = datetime.now()
            fechaformat = fecha.strftime("%m-%d-%Y%H-%M-%S")
            with open(f'archivosEnc/MensajeEnc-{fechaformat}.txt', 'w') as fichero:
                fichero.write(cadena)
            QMessageBox.about(self, "Archivo", "Datos Almacenados Correctamente")
        else:
            QMessageBox.about(self, "Error", "No hay texto que se pueda almacenar")

    def cargarArchivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*.txt);; Python Files (*.py)", options = options)
        if fileName:
            with open(fileName, 'r') as fichero:
                mensaje = fichero.read()
            self.txtMensaje.setText(mensaje)
