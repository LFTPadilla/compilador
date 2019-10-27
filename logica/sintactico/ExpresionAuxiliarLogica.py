from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression

"""
    <ExpresionAuxiliarLogica>::= operadorLogico ["!"] <ExpresionLogica>
"""

class AuxiliarLogica(Expression):
    
    def __init__(self,operadorLogico, negacion, expresionLogica):
        
        self.operadorLogico = operadorLogico
        self.negacion = negacion
        self.expresionLogica = expresionLogica
        
    
    def construirArbol(self, arbol):
        
        arbol.setText(0,self.operadorLogico.lexema)
        
        if self.negacion != None:
            nodoNegacion = QtWidgets.QTreeWidgetItem(arbol)
            nodoNegacion.setText(0, "!")
            expresion =  QtWidgets.QTreeWidgetItem(nodoNegacion)
            self.expresionLogica.construirArbol(expresion)
        else:
            expresion =  QtWidgets.QTreeWidgetItem(arbol)
            self.expresionLogica.construirArbol(expresion)    
        
        
        
       
        