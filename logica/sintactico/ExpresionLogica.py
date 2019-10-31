from PyQt5 import QtWidgets

from logica.sintactico.Expresion import Expression

"""
    <ExpresionLogica>::= "!" "{" <ExpresionLogica> "}" |
    "{" <ExpresionLogica "}" [operadorLogicoBinario <ExpresionLogica> ] |
    <ExpresionRelacional> [operadorLogicoBinario <ExpresionRelacional>]
"""

class Logica(Expression):

    def __init__(self, expresionLogica1, expresionLogica2, expresionRelacional1 , operadorLogico, expresionRelacional2):
        self.expresionLogica1 = expresionLogica1
        self.expresionLogica2 = expresionLogica2
        self.expresionRelacional1 = expresionRelacional1
        self.expresionRelacional2 = expresionRelacional2
        self.operadorLogico = operadorLogico

    def construirArbol(self, arbol):
        arbol.setText(0,self.operadorLogico.lexema)
        arbolExp = QtWidgets.QTreeWidgetItem(arbol)

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
            

                       

               
               
               
               
               
               
           
           
            
        
        