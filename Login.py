from FrmLogin import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.label_2.setText("Hola Mundo")
        self.btnAceptar.clicked.connect(self.validar)

    def validar(self):
        usuario = self.txtUsuario.text()
        contrasena = self.txtContrasena.text()

        if usuario == "Abdiel" and contrasena == "1234":
            print("La contraseña y el usuario son correctos")
        else:
            print("El usuario o la contraseña son incorrectos")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()