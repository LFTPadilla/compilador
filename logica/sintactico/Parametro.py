from PyQt5 import QtWidgets
"""
    <Parametro> ::= <TipoDato> identificador
"""  
class Parameter:
    def __init__(self,tipoRetorno, identificador):
        self.tipoRetorno = tipoRetorno
        self.identificador = identificador

    def __repr__(self):
        return "(Parametro: tipoRetorno: %s, identificador: %s)" % (self.tipoRetorno, self.identificador)

    def __str__(self):
        return "Parametro [%s, %s]" % (self.tipoRetorno, self.identificador)

    def construirArbol(self, arbol, n):
        arbolParametro = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Parametro "+str(n)
        arbolParametro.setText(0,titulo)

        ramaRetorno = QtWidgets.QTreeWidgetItem(arbolParametro)
        ramaRetorno.setText(0,"TipoRetorno "+self.tipoRetorno.lexema)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolParametro)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)
