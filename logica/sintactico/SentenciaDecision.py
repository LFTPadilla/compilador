from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <Decision>::= <sentenciaif>[<sentenciaElse>]
"""
class Decision(Sentence):

    def __init__(self,sentenciaIf, sentenciaElse):
        self.sentenciaIf = sentenciaIf
        self.sentenciaElse = sentenciaElse


    def __repr__(self):
        return "(Sentencia If Else: SentenciasIF: %s, SentenciasELSE: %s)" % (self.sentenciaIf, self.sentenciaElse)

    def __str__(self):
        return "Sentencia Decision [%s, %s]"% (self.sentenciaIf, self.sentenciaElse)
    
    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos):
        pass

    def construirArbol(self, arbol):
        arbolDecision = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Decision "
        arbolDecision.setText(0,titulo)

        self.sentenciaIf.construirArbol(arbolDecision)

        if self.sentenciaElse != None:
            self.sentenciaElse.construirArbol(arbolDecision)