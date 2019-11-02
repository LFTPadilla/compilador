from logica.semantica.TablaSimbolos import SymbolTable
from logica.sintactico.Error import errorSintactico

class ASemantico:

    

    def __init__ (self, unidadCompilacion):
        self.uc = unidadCompilacion
        self.tablaSimbolos = None
        self.listaErrores = []

        
    def llenarTablaSimbolos (self):
        self.uc.llenarTablaSimbolos(self.tablaSimbolos,self.listaErrores)
    
    def analizarSemantica(self):
		self.uc.analizarSemantica(self.tablaSimbolos, self.listaErrores);

