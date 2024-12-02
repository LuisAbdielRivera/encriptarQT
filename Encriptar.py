#pip install cryptography
import base64
from views.FrmEncriptar import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Encriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.btnEncriptar.clicked.connect(self.encriptarAES)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)
        self.btnGuardarArchivo.clicked.connect(self.crearArchivos)
        self.btnCargarArchivo.clicked.connect(self.cargarArchivo)

        self.btnCargarImagen.clicked.connect(self.cargarImagen)
        self.btnLimpiarImg.clicked.connect(self.limpiarCamposImagen)
        self.btnEncriptarImagen.clicked.connect(self.encriptarImgAES)
        self.btnGuardarArchivoImg.clicked.connect(self.crearArchivosImg)

    #Texto
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

    #Imagenes
    def encriptarImgAES(self):
        if not hasattr(self, 'rutaImagen') or not self.rutaImagen:
            return

        with open(self.rutaImagen, "rb") as f:
            data = f.read()

        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        encryptedImg = base64.b64encode(ciphertext).decode('utf-8')
        self.lblImagenEncriptada.setText(encryptedImg)
        print("Imagen Encriptada Correctamente")

    def crearArchivosImg(self):
        cadena = self.lblImagenEncriptada.text()
        if cadena != "":
            fecha = datetime.now()
            fechaformat = fecha.strftime("%m-%d-%Y%H-%M-%S")
            with open(f'archivosImgEnc/ImagenEnc-{fechaformat}.txt', 'w') as fichero:
                fichero.write(cadena)
            QMessageBox.about(self, "Archivo", "Datos Almacenados Correctamente")
        else:
            QMessageBox.about(self, "Error", "No hay texto que se pueda almacenar")

    def cargarImagen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.jpeg);;Todos los Archivos (*)", options=options
        )

        if fileName:
            pixmap = QPixmap(fileName)
            self.lblMensajeImagen.setPixmap(pixmap)
            self.rutaImagen = fileName

    def limpiarCamposImagen(self):
        self.lblMensajeImagen.clear()
        self.lblImagenEncriptada.clear()
        if hasattr(self, 'rutaImagen'):
            del self.rutaImagen