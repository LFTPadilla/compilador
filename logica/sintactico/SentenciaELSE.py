from PyQt5 import QtWidgets
"""
    <SentenciaElse>::= else <BloqueSentencia>
"""
class SentELSE:

    def __init__(self, bloqueSentencias):
        self.bloqueSentencias = bloqueSentencias

    def __repr__(self):
        return "(Sentencia Else : bloqueSentencias: %s)" % (self.bloqueSentencias)

    def __str__(self):
        return "Sentencia Else [%s]"% (self.bloqueSentencias)
                
    def construirArbol(self, arbol):
        arbolElse = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Else"
        arbolElse.setText(0,titulo)
        
        self.bloqueSentencias.construirArbol(arbolElse)

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
       self.sentenciaIf.llenarTablaSimbolos(tablaSimbolos,erroresSemanticos,ambito)
       
    def analisisSemantico(self,tablaSimbolos,listaErrores):
        pass