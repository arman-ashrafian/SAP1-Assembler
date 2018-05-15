import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import assembler as sap1
from mainwindow import Ui_MainWindow

# Enable High-DPI Scaling
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.errorMessage.hide()

        # connect buttons
        self.assembleButton.clicked.connect(lambda: self.assembleClicked())
        self.disassemButton.clicked.connect(lambda: self.disassemClicked())

    def assembleClicked(self):
        code = self.assembly.toPlainText().upper()
        tokens = sap1.tokenize(code)
        obj = sap1.parse(tokens)

        if type(obj) == str:
            self.errorMessage.setText(obj)
            self.errorMessage.show()
            self.errorMessage.setStyleSheet("color: rgb(200,10,10);")
            self.binary.setPlainText("")
        else:
            self.errorMessage.show()
            self.errorMessage.setStyleSheet("color: black")
            self.errorMessage.setText("Assembling...")
            self.outputBinary(obj)
            self.errorMessage.setText("Done.")

    def disassemClicked(self):
        code = self.binary.toPlainText()
        tokens = sap1.tokenize(code)
        asm = sap1.disassemble(tokens)

        if type(asm) == str:
            self.errorMessage.setText(asm)
            self.errorMessage.show()
            self.errorMessage.setStyleSheet("color: rgb(200,10,10);")
            self.assembly.setPlainText("")
        else:
            self.errorMessage.show()
            self.errorMessage.setStyleSheet("color: black")
            self.errorMessage.setText("Assembling...")
            self.outputAsm(asm)
            self.errorMessage.setText("Done.")
        
    def outputAsm(self, asm):
        code = ""
        for line in asm:
            code += line
            code += '\n'
        self.assembly.setPlainText(code)

    def outputBinary(self, obj):
        code = ""
        for e in obj:
            code += e
        self.binary.setPlainText(code)

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(1200, 720)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()