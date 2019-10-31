from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression

"""
    <ExpresionAuxiliarLogica>::= operadorLogico ["!"] <ExpresionLogica>
"""

class AuxiliarLogica(Expression):
    
    def __init__(self, negacion, expresionRelacional):
        
        self.negacion = negacion
        self.expresionRelacional = expresionRelacional
        
    
    def construirArbol(self, arbol):
        pass
       
        