# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmDesencriptar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmDesencriptar(object):
    def setupUi(self, FrmDesencriptar):
        FrmDesencriptar.setObjectName("FrmDesencriptar")
        FrmDesencriptar.resize(690, 512)
        self.centralwidget = QtWidgets.QWidget(FrmDesencriptar)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 711, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblMensajeEncriptado = QtWidgets.QLabel(self.tab)
        self.lblMensajeEncriptado.setGeometry(QtCore.QRect(20, 40, 471, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMensajeEncriptado.setFont(font)
        self.lblMensajeEncriptado.setText("")
        self.lblMensajeEncriptado.setObjectName("lblMensajeEncriptado")
        self.btnDesencriptar = QtWidgets.QPushButton(self.tab)
        self.btnDesencriptar.setGeometry(QtCore.QRect(510, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnDesencriptar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagenes/desencriptado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDesencriptar.setIcon(icon)
        self.btnDesencriptar.setObjectName("btnDesencriptar")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnLimpiar = QtWidgets.QPushButton(self.tab)
        self.btnLimpiar.setGeometry(QtCore.QRect(510, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnLimpiar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Imagenes/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon1)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnCargarArchivo = QtWidgets.QPushButton(self.tab)
        self.btnCargarArchivo.setGeometry(QtCore.QRect(510, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnCargarArchivo.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Imagenes/cargando.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCargarArchivo.setIcon(icon2)
        self.btnCargarArchivo.setObjectName("btnCargarArchivo")
        self.lblMensajeDesencriptado = QtWidgets.QLabel(self.tab)
        self.lblMensajeDesencriptado.setGeometry(QtCore.QRect(20, 250, 471, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMensajeDesencriptado.setFont(font)
        self.lblMensajeDesencriptado.setText("")
        self.lblMensajeDesencriptado.setObjectName("lblMensajeDesencriptado")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btnDesencriptarImg = QtWidgets.QPushButton(self.tab_2)
        self.btnDesencriptarImg.setGeometry(QtCore.QRect(510, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnDesencriptarImg.setFont(font)
        self.btnDesencriptarImg.setIcon(icon)
        self.btnDesencriptarImg.setObjectName("btnDesencriptarImg")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ImgEnc = QtWidgets.QLabel(self.tab_2)
        self.ImgEnc.setGeometry(QtCore.QRect(20, 40, 471, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImgEnc.setFont(font)
        self.ImgEnc.setText("")
        self.ImgEnc.setObjectName("ImgEnc")
        self.btnCargarArchivoImg = QtWidgets.QPushButton(self.tab_2)
        self.btnCargarArchivoImg.setGeometry(QtCore.QRect(510, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnCargarArchivoImg.setFont(font)
        self.btnCargarArchivoImg.setIcon(icon2)
        self.btnCargarArchivoImg.setObjectName("btnCargarArchivoImg")
        self.btnLimpiarImg = QtWidgets.QPushButton(self.tab_2)
        self.btnLimpiarImg.setGeometry(QtCore.QRect(510, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnLimpiarImg.setFont(font)
        self.btnLimpiarImg.setIcon(icon1)
        self.btnLimpiarImg.setObjectName("btnLimpiarImg")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Img = QtWidgets.QLabel(self.tab_2)
        self.Img.setGeometry(QtCore.QRect(20, 250, 471, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Img.setFont(font)
        self.Img.setText("")
        self.Img.setObjectName("Img")
        self.btnGuardarImg = QtWidgets.QPushButton(self.tab_2)
        self.btnGuardarImg.setGeometry(QtCore.QRect(510, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnGuardarImg.setFont(font)
        self.btnGuardarImg.setIcon(icon1)
        self.btnGuardarImg.setObjectName("btnGuardarImg")
        self.tabWidget.addTab(self.tab_2, "")
        FrmDesencriptar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmDesencriptar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName("menubar")
        FrmDesencriptar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmDesencriptar)
        self.statusbar.setObjectName("statusbar")
        FrmDesencriptar.setStatusBar(self.statusbar)

        self.retranslateUi(FrmDesencriptar)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FrmDesencriptar)

    def retranslateUi(self, FrmDesencriptar):
        _translate = QtCore.QCoreApplication.translate
        FrmDesencriptar.setWindowTitle(_translate("FrmDesencriptar", "MainWindow"))
        self.label_2.setText(_translate("FrmDesencriptar", "Mensaje Desencriptado"))
        self.btnDesencriptar.setText(_translate("FrmDesencriptar", "Desencriptar"))
        self.label.setText(_translate("FrmDesencriptar", "Mensaje Encriptado"))
        self.btnLimpiar.setText(_translate("FrmDesencriptar", "Limpiar"))
        self.btnCargarArchivo.setText(_translate("FrmDesencriptar", "Cargar Archivo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("FrmDesencriptar", "Desencriptar Texto"))
        self.btnDesencriptarImg.setText(_translate("FrmDesencriptar", "Desencriptar"))
        self.label_3.setText(_translate("FrmDesencriptar", "Mensaje Desencriptado"))
        self.btnCargarArchivoImg.setText(_translate("FrmDesencriptar", "Cargar Archivo"))
        self.btnLimpiarImg.setText(_translate("FrmDesencriptar", "Limpiar"))
        self.label_4.setText(_translate("FrmDesencriptar", "Mensaje Encriptado"))
        self.btnGuardarImg.setText(_translate("FrmDesencriptar", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("FrmDesencriptar", "Desencriptar Imagen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDesencriptar = QtWidgets.QMainWindow()
    ui = Ui_FrmDesencriptar()
    ui.setupUi(FrmDesencriptar)
    FrmDesencriptar.show()
    sys.exit(app.exec_())
