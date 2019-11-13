from PyQt5 import QtWidgets
"""
    <Parametro> ::= <TipoDato> identificador
"""  
class Parameter:
    def __init__(self,tipoDato, identificador):
        self.tipoDato = tipoDato
        self.identificador = identificador

    def __repr__(self):
        return "(Parametro: tipoDato: %s, identificador: %s)" % (self.tipoDato, self.identificador)

    def __str__(self):
        return "Parametro [%s, %s]" % (self.tipoDato, self.identificador)

    def construirArbol(self, arbol, n):
        arbolParametro = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Parametro "+str(n)
        arbolParametro.setText(0,titulo)

        ramaDato = QtWidgets.QTreeWidgetItem(arbolParametro)
        ramaDato.setText(0,"TipoDato "+self.tipoDato.lexema)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolParametro)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

    def obtenerPythonCode(self):
        return self.identificador.obtenerPythonCode()

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    