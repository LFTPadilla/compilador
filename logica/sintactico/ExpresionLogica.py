from PyQt5 import QtWidgets

from logica.sintactico.Expresion import Expression

"""
    <ExpresionLogica>::= "!" <ExpresionLogica> [<ExpresionAuxiliarLogica>] |  <ExpresionRelacional> [<ExpresionAuxiliarLogica>]
"""

class Logica(Expression):

    def __init__(self, expresionLogica1, expresionLogica2, expresionAuxLogica1 , operadorLogico, expresionAuxLogica2):
        self.expresionLogica1 = expresionLogica1
        self.expresionAuxLogica1 = expresionAuxLogica1
        self.expresionAuxLogica2 = expresionAuxLogica2
        self.operadorLogico = operadorLogico

    def construirArbol(self, arbol):
        
        pass

                       

               
               
               
               
               
               
           
           
            
        
        