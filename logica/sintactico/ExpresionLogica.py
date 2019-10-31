from PyQt5 import QtWidgets

from logica.sintactico.Expresion import Expression

"""
    <ExpresionLogica>::= "!" <ExpresionLogica> [<ExpresionAuxiliarLogica>] |  <ExpresionRelacional> [<ExpresionAuxiliarLogica>]
"""

class Logica(Expression):

    def __init__(self, expresionLogica1, expresionLogica2, expresionRelacional1 , operadorLogico, expresionRelacional2):
        self.expresionLogica1 = expresionLogica1
        self.expresionRelacional1 = expresionRelacional1
        self.expresionRelacional2 = expresionRelacional2
        self.operadorLogico = operadorLogico

    def construirArbol(self, arbol):
        
        pass

                       

               
               
               
               
               
               
           
           
            
        
        