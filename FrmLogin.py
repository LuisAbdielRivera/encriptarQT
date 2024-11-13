# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.lblUsuario.setGeometry(QtCore.QRect(240, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setObjectName("lblUsuario")
        self.lblContrasena = QtWidgets.QLabel(self.centralwidget)
        self.lblContrasena.setGeometry(QtCore.QRect(240, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblContrasena.setFont(font)
        self.lblContrasena.setObjectName("lblContrasena")
        self.txtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(380, 70, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtContrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.txtContrasena.setGeometry(QtCore.QRect(380, 110, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtContrasena.setFont(font)
        self.txtContrasena.setObjectName("txtContrasena")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(460, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnCancelar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon)
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(290, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnAceptar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagenes/acceso.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAceptar.setIcon(icon1)
        self.btnAceptar.setObjectName("btnAceptar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 121, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Imagenes/imagen-inicio.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 240, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblUsuario.setText(_translate("MainWindow", "Usuario"))
        self.lblContrasena.setText(_translate("MainWindow", "Contrasena"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.btnAceptar.setText(_translate("MainWindow", "Entrar"))
        self.label_2.setText(_translate("MainWindow", "Mensaje de Autenticación"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
