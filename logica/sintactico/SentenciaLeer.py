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

        if self.expresion != None:
            ramaExpresion = QtWidgets.QTreeWidgetItem(arbolLeer)
            ramaExpresion.setText(0,"Expresion ")
            
            arbolExpresion = QtWidgets.QTreeWidgetItem(ramaExpresion)            
            self.expresion.construirArbol(arbolExpresion)

    # IMPORTANTE LEER SOLO PUEDE FUNCIONAR EN UNA ASIGNACION O EN UNA DECLARACION
    def obtenerPythonCode(self, identificador):
        codigo = "cout <<  "+ self.expresion.obtenerPythonCode()+";"
        codigo += "cin >>"+ identificador.obtenerPythonCode() +";"
        return codigo

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    def analisisSemantico(self,tablaSimbolos,listaErrores):
        pass