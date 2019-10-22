from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <Retorno>::= return <Expresion> ";"
"""
class Retorno(Sentence):

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Retorno: expresion: %s)" % (self.expresion)

    def __str__(self):
        return "Sentencia Retorno [%s]"% (self.expresion)
    
    def construirArbol(self, arbol, n):
        arbolRetorno = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Return "+str(n)
        arbolRetorno.setText(0,titulo)

        #self.expresion.contruirArbol(arbolRetorno)