#pip install cryptography
from views.FrmEncriptar import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Encriptar(QtWidgets.QMainWindow, Ui_FrmEncriptar):
    def __init__(self, *args, **kwars ):
        QtWidgets.QMainWindow.__init__(self, *args, **kwars)
        self.setupUi(self)

        self.btnEncriptar.clicked.connect(self.encriptarAES)
        self.btnLimpiar.clicked.connect(self.limpiarCampos)
        self.btnGuardar.clicked.connect(self.guardarDatos)
        self.btnCargar.clicked.connect(self.cargarMensaje)

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

    def guardarDatos(self):
        mensaje_original = self.txtMensaje.toPlainText()
        mensaje_encriptado = self.lblMensajeEncriptado.text()

        with open("C:\Prueba\datos_guardados.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Mensaje Original:\n")
            archivo.write(mensaje_original + "\n\n")
            archivo.write("Mensaje Encriptado:\n")
            archivo.write(mensaje_encriptado + "\n")

        print("Datos PA")

    def cargarMensaje(self):
        try:
            with open("C:\Prueba\datos_guardados.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.readlines()

            mensaje_original = ""
            mensaje_encriptado = ""

            for i, linea in enumerate(contenido):
                if linea.strip() == "Mensaje Original:":
                    mensaje_original = contenido[i + 1].strip()
                elif linea.strip() == "Mensaje Encriptado:":
                    mensaje_encriptado = contenido[i + 1].strip()

            self.txtMensaje.setPlainText(mensaje_original)
            self.lblMensajeEncriptado.setText(mensaje_encriptado)
            print("Archivo cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo no existe. Asegúrate de haber guardado los datos primero.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el archivo: {e}")
