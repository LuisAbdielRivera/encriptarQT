#pip install cryptography
from views.FrmEncriptar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PyQt5.QtWidgets import *
from datetime import *
from PyQt5.QtGui import QPixmap
from PIL import Image
import base64
import io

class Encriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.btnEncriptar.clicked.connect(self.encriptarAES)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)
        self.btnGuardarArchivo.clicked.connect(self.crearArchivos)
        self.btnCargarArchivo.clicked.connect(self.cargarArchivo)

        self.btnCargarImagen.clicked.connect(self.cargarImagen)
        #self.btnLimpiarImg.clicked.connect(self.limpiarCamposImagen)
        self.btnEncriptarImagen.clicked.connect(self.encriptarImagen)
        self.btnGuardarArchivoImg.clicked.connect(self.guardarImagenEncriptada)

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
    def cargarImagen(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(
            self, "Abrir imagen", "", "Imágenes (*.png *.jpg *.jpeg);;Todos los archivos (*)", options=opciones
        )

        if archivo:
            self.imagen_original = archivo
            pixmap = QtGui.QPixmap(archivo)
            self.Img.setPixmap(pixmap.scaled(self.Img.size(), QtCore.Qt.KeepAspectRatio))

    def encriptarImagen(self):
        if not self.imagen_original:
            QMessageBox.warning(self, "Advertencia", "No se ha cargado ninguna imagen para encriptar.")
            return

        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"

        try:
            # Leer la imagen y convertirla en datos binarios
            with open(self.imagen_original, "rb") as img_file:
                datos_imagen = img_file.read()

            # Encriptar los datos
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(datos_imagen) + padder.finalize()

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            self.imagen_encriptada = encryptor.update(padded_data) + encryptor.finalize()

            pixmap = QtGui.QPixmap("Imagenes/limpiar.png")
            self.ImgEnc.setPixmap(pixmap.scaled(self.ImgEnc.size(), QtCore.Qt.KeepAspectRatio))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al encriptar la imagen: {str(e)}")
    
    def guardarImagenEncriptada(self):
        if not self.imagen_encriptada:
            QMessageBox.warning(self, "Advertencia", "No hay imagen encriptada para guardar.")
            return

        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(
            self, "Guardar imagen encriptada", "", "Archivos binarios (*.bin);;Todos los archivos (*)", options=opciones
        )

        if archivo:
            try:
                with open(archivo, "wb") as f:
                    f.write(self.imagen_encriptada)
                QMessageBox.information(self, "Éxito", "Imagen encriptada guardada correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error al guardar la imagen: {str(e)}")