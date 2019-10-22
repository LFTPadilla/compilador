import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
sys.path.append(".") 
from logica.lexico.AnalizadorLexico import ALexico
from logica.sintactico.AnalizadorSintactico import ASintactico

#qtCreatorFile = "compilador/interfaz/interfazQT.ui" # Nombre del archivo aquí.
qtCreatorFile = "interfaz/interfazQT.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    tokens = []

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnLimpiar.clicked.connect(self.limpiarVentanas)
        self.btnAnalisisLexico.clicked.connect(self.AnalisisLexico)
        self.btnAnalisisSintactico.clicked.connect(self.AnalisisSintactico)
        
    def AnalisisSintactico(self):
        Asin = ASintactico(self.tokens,self.treeFunciones)
        Asin.esUnidadDeCompilacion()
        self.treeFunciones.show()
        if len(Asin.listaErrores)!=0:
            for i in Asin.listaErrores:
                self.listViewErrores.addItem(str(i))

    
    def AnalisisLexico(self):
        self.listViewTokens.clear()
        codigo = self.txtCodigo.toPlainText()
        #print(codigo)
        analisisLexico = ALexico(codigo)
        analisisLexico.analizar()
        self.tokens = analisisLexico.tokens
        for i in self.tokens:
            self.listViewTokens.addItem(str(i))

        if len(self.tokens) != 0:
            self.btnAnalisisSintactico.setEnabled(True)
        
        #parent = QtWidgets.QTreeWidgetItem(self.treeFunciones)
        #parent.setText("Unidad de compilación")
        #IMPORTANTE!
        #parent.addChild( analizarSintactico.uniCompilacion.arbol() )
    
    def limpiarVentanas(self):
        self.tokens.clear()
        self.txtCodigo.clear()
        self.listViewTokens.clear()
        self.treeFunciones.clear()
        self.listViewErrores.clear()


            
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())