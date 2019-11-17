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

        ramaExpresionLogica = QtWidgets.QTreeWidgetItem(arbolWhile)
        ramaExpresionLogica.setText(0,"Expresion Logica")

        arbolExpresionLogica = QtWidgets.QTreeWidgetItem(ramaExpresionLogica)
        self.expresionLogica.construirArbol(arbolExpresionLogica)
        
        self.bloqueSentencias.construirArbol(arbolWhile)

    def obtenerPythonCode(self, tabulacion):
        codigo = "while ( "+self.expresionLogica.obtenerPythonCode()+" ):"
        codigo += self.bloqueSentencias.obtenerPythonCode(tabulacion + 1)
        return codigo

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    def analisisSemantico(self,tablaSimbolos,listaErrores):
        pass