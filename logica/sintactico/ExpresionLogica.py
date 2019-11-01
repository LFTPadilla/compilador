from PyQt5 import QtWidgets

from logica.sintactico.Expresion import Expression
from logica.lexico.Categorias import Categoria

"""
    <ExpresionLogica>::= "!" "{" <ExpresionLogica> "}" |
    "{" <ExpresionLogica "}" [operadorLogicoBinario <ExpresionLogica> ] |
    <ExpresionRelacional> [operadorLogicoBinario <ExpresionRelacional>]
"""

class Logica(Expression):

    def __init__(self, operador1, expresionLogica1, operador2, expresionLogica2, expresionLogica3, expresionRelacional, expresionAuxiliarLogica):
        self.operador1 = operador1
        self.expresionLogica1 = expresionLogica1
        self.operador2 = operador2
        self.expresionLogica2 = expresionLogica2
        self.expresionLogica3 = expresionLogica3
        self.expresionRelacional = expresionRelacional
        self.expresionAuxiliarLogica = expresionAuxiliarLogica

    def construirArbol(self, arbol):
       
        if self.expresionRelacional != None:
                     
            if self.expresionAuxiliarLogica != None:
                self.expresionAuxiliarLogica.construirArbol(arbol)                             
                nodoOperadorAux = QtWidgets.QTreeWidgetItem(arbol)
                self.expresionRelacional.construirArbol(nodoOperadorAux)
            else:
                self.expresionRelacional.construirArbol(arbol)        
     
           
       
        if self.operador2 != None:
            arbol.setText(0, self.operador2.lexema)
        
            if self.operador1 != None and self.operador1.lexema == "!":
                nodoNegacion = QtWidgets.QTreeWidgetItem(arbol)
                nodoNegacion.setText(0, self.operador1.lexema)
                ramaNegacion = QtWidgets.QTreeWidgetItem(nodoNegacion)
                self.expresionLogica1.construirArbol(ramaNegacion)
                
                if self.expresionAuxiliarLogica != None:
                    nodoOperadorAux = QtWidgets.QTreeWidgetItem(arbol)
                    self.expresionAuxiliarLogica.construirArbol(nodoOperadorAux)
                    ramaLogica2 = QtWidgets.QTreeWidgetItem(nodoOperadorAux)
                    self.expresionLogica2.construirArbol(ramaLogica2) 
                else:
                    ramaLogica2 = QtWidgets.QTreeWidgetItem(arbol)
                    self.expresionLogica2.construirArbol(ramaLogica2)     
                
            
            elif self.operador1 != None and self.operador1.categoria == Categoria.OperadorLogico:
                nodoOperador1 = QtWidgets.QTreeWidgetItem(arbol)
                nodoOperador1.setText(0, self.operador1.lexema)
                ramaLogica1 = QtWidgets.QTreeWidgetItem(nodoOperador1)
                ramaLogica2 = QtWidgets.QTreeWidgetItem(nodoOperador1)
                
                self.expresionLogica1.construirArbol(ramaLogica1)
                self.expresionLogica2.construirArbol(ramaLogica2)
               
                
                if self.expresionAuxiliarLogica != None:
                    nodoOperadorAux = QtWidgets.QTreeWidgetItem(arbol)
                    self.expresionAuxiliarLogica.construirArbol(nodoOperadorAux)
                    ramaLogica3 = QtWidgets.QTreeWidgetItem(nodoOperadorAux)
                    self.expresionLogica3.construirArbol(ramaLogica3) 
                else:
                    ramaLogica3 = QtWidgets.QTreeWidgetItem(arbol)
                    self.expresionLogica3.construirArbol(ramaLogica3)
                
        else:
            
            if self.operador1 != None and self.operador1.lexema == "!":
                
                arbol.setText(0, self.operador1.lexema)
                ramaNegacion = QtWidgets.QTreeWidgetItem(arbol)
                self.expresionLogica1.construirArbol(ramaNegacion)
                
                    
                
                
                   
                
                
                
                   

        if self.operadorLogico.lexema == "!":

            ramaExpresionLogica = QtWidgets.QTreeWidgetItem(arbolExp)
            self.expresionLogica1.construirArbol(ramaExpresionLogica)

        if self.operadorLogico.lexema != "!":

            if self.expresionLogica1 != None and self.expresionLogica1 != None:
                ramaExpresionLogica1 = QtWidgets.QTreeWidgetItem(arbolExp)
                self.expresionLogica1.construirArbol(ramaExpresionLogica1)

                ramaExpresionLogica2 = QtWidgets.QTreeWidgetItem(arbolExp)
                self.expresionLogica2.construirArbol(ramaExpresionLogica2)
            
            if self.expresionRelacional1 != None and self.expresionRelacional2 != None:
                ramaExpresionRelacional1 = QtWidgets.QTreeWidgetItem(arbolExp)
                self.expresionRelacional1.construirArbol(ramaExpresionRelacional1)

                ramaExpresionRelacional2 = QtWidgets.QTreeWidgetItem(arbolExp)
                self.expresionRelacional2.construirArbol(ramaExpresionRelacional2)
            

                       

               
               
               
               
               
               
           
           
            
        
        