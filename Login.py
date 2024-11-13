from FrmLogin import *
from Menu import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.label_2.setText("Hola Bienvenido a mi App")
        self.btnAceptar.clicked.connect(self.validar)
        self.btnCancelar.clicked.connect(self.salir)

    def validar(self):
        usuario = self.txtUsuario.text()
        contrasena = self.txtContrasena.text()

        if usuario == "Abdiel" and contrasena == "1234":
            self.label_2.setText("Acceso Consedido")
            self.openMenu()
            self.hide()
        else:
            self.label_2.setText("Acceso Denegado")
    
    def salir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Error de usuario o contraseña")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMenssageBox.Ok | QMessageBox.Cancel)
        returnvValue = msgBox.exec()
        if returnvValue == QMenssageBox.Ok:
            self.close()
    
    def openMenu(self):
        opennewwindow = Menu(self)
        opennewwindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()