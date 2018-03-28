import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import assemb as sap1
from mainwindow import Ui_MainWindow

# Enable High-DPI Scaling
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.errorMessage.hide()

        # connect assemble button
        self.assembleButton.clicked.connect(lambda: self.assembleClicked())
	
    def assembleClicked(self):
        code = self.code.toPlainText().upper()
        tokens = sap1.tokenize(code)
        obj = sap1.parse(tokens)
        self.outputCode(obj)
    
    def outputCode(self, obj):
        code = ""
        for e in obj:
            code += e
        self.output.setText(code)

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(800, 480)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()