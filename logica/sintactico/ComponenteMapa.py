from PyQt5 import QtWidgets
"""
    <componenteMap>::= "(" <termino> "," <termino> ")"
"""
class componenteMap:

    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor

    def __repr__(self):
        return "(ComponenteMapa: Llave: %s, Valor: %s)" % (self.llave, self.valor)

    def __str__(self):
        return "ComponenteMapa [%s,%s]" % (self.llave, self.valor)

    def construirArbol(self, arbol, n):
        arbolComponente = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Componente "+str(n)
        arbolComponente.setText(0,titulo)

        ramaLlave = QtWidgets.QTreeWidgetItem(arbolComponente)
        ramaLlave.setText(0,"llave "+ self.llave.lexema)

        ramaValor = QtWidgets.QTreeWidgetItem(arbolComponente)
        ramaValor.setText(0,"valor "+ self.valor.lexema)

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos):
        pass