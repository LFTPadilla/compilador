from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <Leer>::= leer "(" [<expresion>] ")" ";"
"""
class Leer(Sentence):

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Leer: expresion: %s)" % (self.expresion)

    def __str__(self):
        return "Sentencia Leer [%s]"% (self.expresion)
    
    def construirArbol(self, arbol):
        arbolLeer = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Leer "
        arbolLeer.setText(0,titulo)

        #if self.expresion != None:
        #    self.expresion.contruirArbol(arbolLeer)