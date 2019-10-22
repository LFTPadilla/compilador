from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <Imprimir>::= imprimir "(" [<expresion>] ")" ";"
"""
class Imprimir(Sentence):

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Imprimir: expresion: %s)" % ( self.expresion)

    def __str__(self):
        return "Sentencia Imprimir [%s]" % (self.expresion)
    
    def construirArbol(self, arbol, n):
        arbolImprimir = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Imprimir "+str(n)
        arbolImprimir.setText(0,titulo)

        #self.expresion.construirArbol(arbolImprimir)

        

    