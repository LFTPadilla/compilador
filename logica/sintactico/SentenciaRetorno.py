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
    
    def construirArbol(self, arbol):
        arbolRetorno = QtWidgets.QTreeWidgetItem(arbol)
        arbolRetorno.setText(0,"Return")

        ramaExpresion = QtWidgets.QTreeWidgetItem(arbolRetorno)
        ramaExpresion.setText(0,"Expresion ")
            
        arbolExpresion = QtWidgets.QTreeWidgetItem(ramaExpresion)            
        self.expresion.construirArbol(arbolExpresion)
    

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    