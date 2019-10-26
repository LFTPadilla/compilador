from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <Ciclo>::= while "(" <expresionLogica> ")" <bloqueSentencia>
"""
class SentenceWhile(Sentence):

    def __init__(self, expresionLogica, bloqueSentencias):
        self.expresionLogica = expresionLogica
        self.bloqueSentencias = bloqueSentencias

    def __repr__(self):
        return "(Sentencia While: expresionLogica: %s, bloqueSetnecias: %s)" % (self.expresionLogica, self.bloqueSentencias)

    def __str__(self):
        return "Sentencia While [%s, %s]"% (self.expresionLogica, self.bloqueSentencias)
    
    def construirArbol(self, arbol):
        arbolWhile = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "While "
        arbolWhile.setText(0,titulo)

        #self.expresionLogica.construirArbol(arbolWhile)
        
        self.bloqueSentencias.construirArbol(arbolWhile)