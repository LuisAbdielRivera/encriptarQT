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
        FrmDesencriptar.resize(690, 513)
        self.centralwidget = QtWidgets.QWidget(FrmDesencriptar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 50, 481, 161))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 471, 171))
        self.label_3.setObjectName("label_3")
        FrmDesencriptar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmDesencriptar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName("menubar")
        FrmDesencriptar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmDesencriptar)
        self.statusbar.setObjectName("statusbar")
        FrmDesencriptar.setStatusBar(self.statusbar)

        self.retranslateUi(FrmDesencriptar)
        QtCore.QMetaObject.connectSlotsByName(FrmDesencriptar)

    def retranslateUi(self, FrmDesencriptar):
        _translate = QtCore.QCoreApplication.translate
        FrmDesencriptar.setWindowTitle(_translate("FrmDesencriptar", "MainWindow"))
        self.label.setText(_translate("FrmDesencriptar", "Mensaje"))
        self.pushButton.setText(_translate("FrmDesencriptar", "Desencriptar"))
        self.pushButton_2.setText(_translate("FrmDesencriptar", "Cargar Archivo"))
        self.pushButton_3.setText(_translate("FrmDesencriptar", "Limpiar"))
        self.pushButton_4.setText(_translate("FrmDesencriptar", "Guardar Archivo"))
        self.label_2.setText(_translate("FrmDesencriptar", "Desencriptado"))
        self.label_3.setText(_translate("FrmDesencriptar", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDesencriptar = QtWidgets.QMainWindow()
    ui = Ui_FrmDesencriptar()
    ui.setupUi(FrmDesencriptar)
    FrmDesencriptar.show()
    sys.exit(app.exec_())