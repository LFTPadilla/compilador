import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
sys.path.append(".") 
from logica.lexico.AnalizadorLexico import ALexico
from logica.sintactico.AnalizadorSintactico import ASintactico
from logica.semantica.AnalizadorSemantico import ASemantico

#qtCreatorFile = "compilador/interfaz/interfazQT.ui" # Nombre del archivo aquí.
qtCreatorFile = "interfaz/interfazQT.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    tokens = []
    ASin = None
    ASem = None

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnAnalisisLexico.clicked.connect(self.AnalisisLexico)
        self.btnAnalisisSintactico.clicked.connect(self.AnalisisSintactico)
        self.btnAnalisis.clicked.connect(self.AnalisisCompleto)
    
    def AnalisisCompleto(self):
        self.AnalisisLexico()
        self.AnalisisSintactico()
        self.AnalisisSemantico()


    #Analisador Semantico
    def AnalisisSemantico(self):

        self.ASem = ASemantico(self.ASin.unidadCompilacion)
        self.ASem.llenarTablaSimpolos()
        if len(self.ASem.listaErrores)!=0:
            self.tabErrores.setCurrentIndex(2)
            for i in self.ASem.listaErrores:
                self.listViewErroresSintacticos.addItem(str(i))
    
    def AnalisisSintactico(self):
        self.ASin = ASintactico(self.tokens,self.treeFunciones)
        self.ASin.esUnidadDeCompilacion()

        self.treeFunciones.show()
        if len(self.ASin.listaErrores)!=0:
            self.tabErrores.setCurrentIndex(1)
            for i in self.ASin.listaErrores:
                self.listViewErroresSintacticos.addItem(str(i))
        else:
            self.btnAnalisisSemantico.setEnabled(True)


    
    def AnalisisLexico(self):

        self.limpiar()  
        codigo = self.txtCodigo.toPlainText()
    
        if len(codigo)==0:
            return False

        analisisLexico = ALexico(codigo)
        analisisLexico.analizar()
        print(analisisLexico.listaErrores)
        self.tokens = analisisLexico.tokens
        for i in self.tokens:
            self.listViewTokens.addItem(str(i))
        
        if len(analisisLexico.listaErrores) !=0:
            self.tabErrores.setCurrentIndex(0)
            for err in analisisLexico.listaErrores:
                self.listViewErroresLexicos.addItem(str(err))
        elif len(self.tokens) != 0:
            self.btnAnalisisSintactico.setEnabled(True)
            

    
    def limpiar(self):
        self.tokens = []
        self.ASin = None 
        self.ASem = None       
        self.listViewTokens.clear()
        self.treeFunciones.clear()
        self.listViewErroresSintacticos.clear()
        self.listViewErroresLexicos.clear()
        self.listViewErroresSemanticos.clear()
        self.btnAnalisisSintactico.setEnabled(False)
        self.btnAnalisisSemantico.setEnabled(False)


            
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
    
    
    