import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.Qt import Qt
sys.path.append(".") 
from logica.lexico.AnalizadorLexico import Analizador

qtCreatorFile = "interfaz/interfazQT.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnAnalizar.clicked.connect(self.AnalisisLexico)

        for i in range(3):
            parent = QtWidgets.QTreeWidgetItem(self.treeWidget)
            parent.setText(0, "Parent {}".format(i))
            #parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            for x in range(5):
                child = QtWidgets.QTreeWidgetItem(parent)
                #child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, "Child {}".format(x))
                #child.setCheckState(0, Qt.Unchecked)
        self.treeWidget.show()

    def AnalisisLexico(self):
        self.listViewTokens.clear()
        codigo = self.txtCodigo.toPlainText()
        #print(codigo)
        analisisLexico = Analizador(codigo)
        analisisLexico.analizar()
        tokens = analisisLexico.tokens
        for i in tokens:
            self.listViewTokens.addItem(str(i))


        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())