import abc
from abc import ABC

class Expression(ABC):
    
    __metaclass__ = ABC


    def __init_(self):
        pass

    def construirArbol(self, arbol, n):
        pass

    def analisisSemantico(self,tablaSimbolos,listaErrores):
        pass

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    
    def obtenerTipoDato(self):
        pass