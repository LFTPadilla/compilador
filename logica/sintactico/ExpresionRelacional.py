from logica.sintactico.Expresion import Expression
from PyQt5 import QtWidgets

class Relacional(Expression):

    def __init__(self, expresionAritmetica1,operadorRelacional, expresionAritmetica2):
        self.expresionAritmetica1 = expresionAritmetica1
        self.operadorRelacional = operadorRelacional
        self.expresionAritmetica2 = expresionAritmetica2

    def construirArbol(self, arbol):
        #Los arboles en realidad son nodos de partida o raices
        #llega el 'arbol' nodo 'R'

        if self.operadorRelacional != None :
            arbol.setText(0,self.operadorRelacional.lexema)

            ramaExpresion1 = QtWidgets.QTreeWidgetItem(arbol)
            self.expresionAritmetica1.construirArbol(ramaExpresion1)
            
            ramaExpresion2 = QtWidgets.QTreeWidgetItem(arbol)
            self.expresionAritmetica2.construirArbol(ramaExpresion2)
            
        elif self.expresionArimetica1 != None and self.operadorRelacional == None:            
            self.expresionAritmetica1.construirArbol(arbol)


    

    def __repr__(self):
        return "(Expresion relaciona:  %s eAuxArit:: %s termino: %s)" % (self.expresionRelacional, self.expresionAuxiliarRelacional, self.termino)

    def __str__(self):
        return "ExpresionRelaciona:  %s eAuxArit:: %s termino: %s)" % (self.expresionRelacional, self.expresionAuxiliarRelacional, self.termino)
    