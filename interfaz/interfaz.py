import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
sys.path.append(".") 
from logica.lexico.AnalizadorLexico import ALexico
from logica.sintactico.AnalizadorSintactico import ASintactico

qtCreatorFile = "interfaz/interfazQT.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    arbol = None
    tokens = []

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnLimpiar.clicked.connect(self.limpiarVentanas)
        self.btnAnalisisLexico.clicked.connect(self.AnalisisLexico)
        self.btnAnalisisSintactico.clicked.connect(self.AnalisisSintactico)
        self.arbol = self.treeFunciones
        self.arbol.clear()
        


    def AnalisisSintactico(self):
        Asin = ASintactico(self.tokens,self.arbol)
        Asin.esUnidadDeCompilacion()




    def construirArbol(self):
        #QtWidgets.QTreeWidgetItem(self.treeFunciones)  
        for i in range(3):
            parent = QtWidgets.QTreeWidgetItem(self.treeFunciones)
            
            parent.setText(0, "Parent {}".format(i))
            #parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            for x in range(5):
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setText(0, "Padre")
                #child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                hijo1 = QtWidgets.QTreeWidgetItem()
                hijo1.setText(0, "Hijo 1")
                
                child.addChild( hijo1)
                #child.setCheckState(0, Qt.Unchecked)
        self.treeFunciones.show()

    
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
        self.txtCodigo.clear()
        self.listViewTokens.clear()
        self.treeFunciones.clear()


            
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())