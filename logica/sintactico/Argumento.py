from PyQt5 import QtWidgets
"""
    <Argumento>::= identificador | <expresion>
"""
class Argument:

    def __init__(self, identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion

    def __repr__(self):
        return "(Argumento:  identificador: %s  expresion: %s)" % (self.identificador, self.expresion)

    def __str__(self):
        return "Argumento [ %s, %s]"% (self.identificador, self.expresion)

    def construirArbol(self, arbol, n):
        arbolArgumento = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Argumento "+str(n)
        arbolArgumento.setText(0, titulo)

        if self.identificador == None:
            self.expresion.construirArbol(arbolArgumento)

        elif self.expresion == None:
            ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolArgumento)
            ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

    def obtenerPythonCode(self):
        codigo = ""
        if self.identificador == None:
            codigo += self.expresion.obtenerPythonCode()
        elif self.expresion == None:
            codigo += self.identificador.obtenerPythonCode()
        return codigo

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass