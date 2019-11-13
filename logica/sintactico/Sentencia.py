import abc
from abc import ABC

class Sentence(ABC):

    __metaclass__ = ABC

    def __init__(self):
        pass
    

    def construirArbol(self, arbol, n):
        pass

    def analizarSemantica(self):
        pass
    
    def obtenerPythonCode(self):
        pass
    
    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    