from logica.semantica.TablaSimbolos import simbolito
from logica.sintactico.Error import errorSintactico

class ASemantico:

    tablaSimbolos = None
    listaErrores = []

    def __init__ (self, unidadCompilacion):
        self.uc = unidadCompilacion
        
    def llenarTablaSimpolos (self):
        self.uc.llenarTablaSimbolos(self.tablaSimbolos,self.listaErrores)
    
    
