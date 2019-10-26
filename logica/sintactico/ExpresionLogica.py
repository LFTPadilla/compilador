from PyQt5 import QtWidgets

from logica.sintactico.Expresion import Expression

"""
    <ExpresionLogica>::= "!" <ExpresionRelacional> | <ExpresionRelacional1> operadorLogico <ExpresionRelacional2> | <ExpresionRelacional>
"""

class Logica(Expression):

    def __init__(self, operadorLogico, expresionRelacional1, expresionRelacional2, expresionAuxiliarLogica):
        self.operadorLogico = operadorLogico
        self.expresionRelacional1 = expresionRelacional1
        self.expresionRelacional2 = expresionRelacional2

    def construirArbol(self, arbol):
        
        if(self.operadorLogico != None):
            
            arbol.setText(0,self.operadorLogico.lexema)
            
            arbolRelacional1 = QtWidgets.QTreeWidgetItem(arbol)
            self.expresionRelacional1.construirArbol(arbolRelacional1)           
            
            if self.expresionRelacional2 != None:
                
                arbolRelacional2 = QtWidgets.QTreeWidgetItem(arbol)
                self.expresionRelacional2.construirArbol(arbolRelacional2)
        else:
            self.expresionRelacional1.construirArbol(arbol)    
            
        
        