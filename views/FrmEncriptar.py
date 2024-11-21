# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmEncriptar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmEncriptar(object):
    def setupUi(self, FrmEncriptar):
        FrmEncriptar.setObjectName("FrmEncriptar")
        FrmEncriptar.resize(708, 539)
        self.centralwidget = QtWidgets.QWidget(FrmEncriptar)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 711, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtMensaje = QtWidgets.QTextEdit(self.tab)
        self.txtMensaje.setGeometry(QtCore.QRect(10, 40, 481, 161))
        self.txtMensaje.setObjectName("txtMensaje")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblMensajeEncriptado = QtWidgets.QLabel(self.tab)
        self.lblMensajeEncriptado.setGeometry(QtCore.QRect(50, 260, 471, 171))
        self.lblMensajeEncriptado.setObjectName("lblMensajeEncriptado")
        self.btnEncriptar = QtWidgets.QPushButton(self.tab)
        self.btnEncriptar.setGeometry(QtCore.QRect(510, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnEncriptar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagenes/encriptado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEncriptar.setIcon(icon)
        self.btnEncriptar.setObjectName("btnEncriptar")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnLimpiar = QtWidgets.QPushButton(self.tab)
        self.btnLimpiar.setGeometry(QtCore.QRect(510, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnLimpiar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Imagenes/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon1)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnCargar = QtWidgets.QPushButton(self.tab)
        self.btnCargar.setGeometry(QtCore.QRect(510, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnCargar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Imagenes/cargando.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCargar.setIcon(icon2)
        self.btnCargar.setObjectName("btnCargar")
        self.btnGuardar = QtWidgets.QPushButton(self.tab)
        self.btnGuardar.setGeometry(QtCore.QRect(510, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btnGuardar.setFont(font)
        self.btnGuardar.setObjectName("btnGuardar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        FrmEncriptar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmEncriptar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 21))
        self.menubar.setObjectName("menubar")
        FrmEncriptar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmEncriptar)
        self.statusbar.setObjectName("statusbar")
        FrmEncriptar.setStatusBar(self.statusbar)

        self.retranslateUi(FrmEncriptar)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FrmEncriptar)

    def retranslateUi(self, FrmEncriptar):
        _translate = QtCore.QCoreApplication.translate
        FrmEncriptar.setWindowTitle(_translate("FrmEncriptar", "MainWindow"))
        self.label_2.setText(_translate("FrmEncriptar", "Encriptado"))
        self.lblMensajeEncriptado.setText(_translate("FrmEncriptar", "TextLabel"))
        self.btnEncriptar.setText(_translate("FrmEncriptar", "Encriptar"))
        self.label.setText(_translate("FrmEncriptar", "Mensaje"))
        self.btnLimpiar.setText(_translate("FrmEncriptar", "Limpiar"))
        self.btnCargar.setText(_translate("FrmEncriptar", "Cargar Archivo"))
        self.btnGuardar.setText(_translate("FrmEncriptar", "Guardar Archivo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("FrmEncriptar", "Encriptar Texto"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("FrmEncriptar", "Encriptar Imagen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmEncriptar = QtWidgets.QMainWindow()
    ui = Ui_FrmEncriptar()
    ui.setupUi(FrmEncriptar)
    FrmEncriptar.show()
    sys.exit(app.exec_())
