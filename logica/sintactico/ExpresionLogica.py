from PyQt5 import QtWidgets

from logica.sintactico.Expresion import Expression

"""
    <ExpresionLogica>::= "!" <ExpresionLogica> [<ExpresionAuxiliarLogica>] |  <ExpresionRelacional> [<ExpresionAuxiliarLogica>]
"""

class Logica(Expression):

    def __init__(self, negacion, expresionLogica, expresionRelacional , expresionAuxiliarLogica):
        self.negacion = negacion
        self.expresionLogica = expresionLogica
        self.expresionRelacional = expresionRelacional
        self.expresionAuxiliarLogica = expresionAuxiliarLogica

    def construirArbol(self, arbol):
        
        if self.expresionAuxiliarLogica != None:
           
           self.expresionAuxiliarLogica.construirArbol(arbol)
           
           arbolExpresion = QtWidgets.QTreeWidgetItem(arbol)
                      
           if self.negacion != None:
               arbolExpresion.setText(0, "!")
               arbolExpresionLogicaNegada = QtWidgets.QTreeWidgetItem(arbolExpresion)
               self.expresionLogica.construirArbol(arbolExpresionLogicaNegada)
           else:
               self.expresionRelacional.construirArbol(arbolExpresion)
        
        else:
            if self.negacion != None:
               arbol.setText(0,"!")
               arbolExpresionLogicaNegada = QtWidgets.QTreeWidgetItem(arbol)
               self.expresionLogica.construirArbol(arbolExpresionLogicaNegada)
            else:
               self.expresionRelacional.construirArbol(arbol)

                       

               
               
               
               
               
               
           
           
            
        
        