from logica.semantica.TablaSimbolos import SymbolTable
from logica.sintactico.Error import errorSintactico

class ASemantico:

    

    def __init__ (self, unidadCompilacion):
        self.uc = unidadCompilacion
        self.listaErrores = []
        self.tablaSimbolos = SymbolTable(self.listaErrores)
        
    def obtenerPythonCode(self):
        #no se
        pass

    def llenarTablaSimbolos (self):
        self.uc.llenarTablaSimbolos(self.tablaSimbolos,self.listaErrores)
    
