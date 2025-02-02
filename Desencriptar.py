from views.FrmDesencriptar import *
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


class Desencriptar(QtWidgets.QMainWindow, Ui_FrmDesencriptar):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.btnDesencriptar.clicked.connect(self.desencriptarAES)
        self.btnCargarArchivo.clicked.connect(self.cargarArchivo)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)

        self.btnCargarArchivoImg.clicked.connect(self.cargarImagenDesencrip)
        self.btnDesencriptarImg.clicked.connect(self.desencriptarImagen)
        self.btnGuardarImg.clicked.connect(self.guardarImagenDesencrip)

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
        self.lblMensajeDesencriptado.clear()

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
        self.lblMensajeDesencriptado.setText(mensaje_desencriptado.decode('utf-8'))

        print(data)

    def cargarImagenDesencrip(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo encriptado", "", "Archivos binarios (*.bin);;Todos los archivos (*)", options=opciones)

        if archivo:
            try:
                with open(archivo, "rb") as f:
                    self.imagen_encriptada = f.read()
                self.ImgEnc.setText("Imagen Cargada Correctamente.")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", f"No se pudo cargar la imagen: {str(e)}")

    def desencriptarImagen(self):
        if not self.imagen_encriptada:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Primero debes cargar una imagen encriptada.")
            return

        try:
            # Clave e IV para desencriptar
            key = b"123456789101112131415161718_UTXJ"
            iv = b"TI_UTXJ2024ENCRI"

            # Desencriptar los datos
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(self.imagen_encriptada) + decryptor.finalize()

            # Convertir datos desencriptados a una imagen
            image_stream = io.BytesIO(decrypted_data)
            image = Image.open(image_stream)

            # Mostrar imagen desencriptada en la interfaz
            image.save("temporal_desencriptada.png")  # Guardar temporalmente para mostrar
            pixmap = QPixmap("temporal_desencriptada.png")
            self.Img.setPixmap(pixmap.scaled(self.Img.size(), QtCore.Qt.KeepAspectRatio))
            self.imagen_desencriptada = image

            # self.TxtImgDesencriptada.setText("Imagen desencriptada correctamente.")
            # self.TxtImgDesencriptada.setStyleSheet("color: green;")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Error al desencriptar la imagen: {str(e)}")

    def guardarImagenDesencrip(self):
        if not self.imagen_desencriptada:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay imagen desencriptada para guardar.")
            return

        opciones = QFileDialog.Options()
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar imagen desencriptada", f"imagen_desencriptada_{fecha}.png", "Archivos de imagen (*.png);;Todos los archivos (*)", options=opciones)

        if archivo:
            try:
                self.imagen_desencriptada.save(archivo, format="PNG")
                QtWidgets.QMessageBox.information(self, "Éxito", "Imagen desencriptada guardada exitosamente.")
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", f"No se pudo guardar la imagen: {str(e)}")
    
