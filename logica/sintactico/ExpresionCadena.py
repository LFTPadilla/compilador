from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression
"""
    <ExpresionCadena>::= cadena [ "+" <Expresion> ] 
"""
class Cadena(Expression):

    def __init__(self, cadenaCaracteres, expresion):
        self.cadenaCaracteres = cadenaCaracteres
        self.expresion = expresion

    def construirArbol(self, arbolExpresionCadena):
        titulo = "Expresion Cadena"
        arbolExpresionCadena.setText(0,titulo)

        ramaCadena = QtWidgets.QTreeWidgetItem(arbolExpresionCadena)
        ramaCadena.setText(0,"Cadena Caracteres "+self.cadenaCaracteres.lexema)

        if self.expresion != None:
            ramaExpresion = QtWidgets.QTreeWidgetItem(arbolExpresionCadena)
            ramaExpresion.setText(0,"Expresion ")

            arbolExpresion = QtWidgets.QTreeWidgetItem(ramaExpresion)
            self.expresion.construirArbol(arbolExpresion)