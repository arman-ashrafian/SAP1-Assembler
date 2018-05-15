# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 720))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(120,120,120);\n"
"    border: none;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: rgb(80,80,80);\n"
"    font-size: 24pt;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"    background-color: rgb(80,80,80);\n"
"    font-size: 24pt;\n"
"}\n"
"\n"
"QPushButton#assembleButton{\n"
"    font-size: 20pt;\n"
"    background-color: rgb(10,100,10)\n"
"}\n"
"\n"
"QPushButton#disassemButton{\n"
"    font-size: 20pt;\n"
"    background-color: rgb(200,0,30)\n"
"}\n"
"")
        self.assembly = QtWidgets.QPlainTextEdit(MainWindow)
        self.assembly.setGeometry(QtCore.QRect(10, 10, 731, 651))
        self.assembly.setObjectName("assembly")
        self.errorMessage = QtWidgets.QLabel(MainWindow)
        self.errorMessage.setGeometry(QtCore.QRect(10, 670, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.errorMessage.setFont(font)
        self.errorMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.errorMessage.setObjectName("errorMessage")
        self.assembleButton = QtWidgets.QPushButton(MainWindow)
        self.assembleButton.setGeometry(QtCore.QRect(760, 670, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.assembleButton.setFont(font)
        self.assembleButton.setObjectName("assembleButton")
        self.binary = QtWidgets.QPlainTextEdit(MainWindow)
        self.binary.setGeometry(QtCore.QRect(760, 10, 421, 651))
        self.binary.setObjectName("binary")
        self.disassemButton = QtWidgets.QPushButton(MainWindow)
        self.disassemButton.setGeometry(QtCore.QRect(990, 670, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.disassemButton.setFont(font)
        self.disassemButton.setObjectName("disassemButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.errorMessage.setText(_translate("MainWindow", "Error Message"))
        self.assembleButton.setText(_translate("MainWindow", "Assemble"))
        self.disassemButton.setText(_translate("MainWindow", "Disassemble"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

