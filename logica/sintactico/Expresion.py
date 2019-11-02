import abc
from abc import ABC

class Expression(ABC):
    
    __metaclass__ = ABC


    def __init_(self):
        pass

    def construirArbol(self, arbol, n):
        pass

    def analizarSemantica(self):
        pass

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos):
        pass