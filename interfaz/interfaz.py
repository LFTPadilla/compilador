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

    

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.tokens = []
        self.ASin = None
        self.ASem = None
        self.uCompilacion = None 
        self.setupUi(self)
        self.btnAnalisisLexico.clicked.connect(self.AnalisisLexico)
        self.btnAnalisisSintactico.clicked.connect(self.AnalisisSintactico)
        self.btnAnalisis.clicked.connect(self.AnalisisCompleto)
        #self.txtCodigo.setText("        public int nombre ( String a ){            a++;            b--;            return (2+1)>b;        }        ")    

    def AnalisisCompleto(self):
        self.AnalisisLexico()
        self.AnalisisSintactico()
        self.AnalisisSemantico()


    #Analisador Semantico
    def AnalisisSemantico(self):
        self.ASem = ASemantico(self.uCompilacion)
        self.ASem.llenarTablaSimbolos()
        self.ASem.analisisSemantico()

        if len(self.ASem.tablaSimbolos.listaSimbolos)!=0:
            self.tabTokenSimbolo.setCurrentIndex(1)
            for i in self.ASem.tablaSimbolos.listaSimbolos:
                self.listViewSimbolos.addItem(str(i))
        
        if len(self.ASem.listaErrores)!=0:
            self.tabErrores.setCurrentIndex(2)
            for i in self.ASem.listaErrores:
                self.listViewErroresSemanticos.addItem(str(i))

       # self.Asem.obtenerPythonCode()
    
    def AnalisisSintactico(self):
        self.ASin = ASintactico(self.tokens,self.treeFunciones)
        self.uCompilacion = self.ASin.esUnidadDeCompilacion()

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
        self.listViewSimbolos.clear()
        self.btnAnalisisSintactico.setEnabled(False)
        self.btnAnalisisSemantico.setEnabled(False)


    def escribirArchivo (self, codigo):
        #ni ideita
        pass

    def traduccion(self):
        #ni ideita
        pass            
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
    
    
    