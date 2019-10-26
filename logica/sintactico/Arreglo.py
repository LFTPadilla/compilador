"""
    <Arreglo>::= array <tipoDato> identificador "=" "[" <listaExpresiones> "]" ";"
"""
from PyQt5 import QtWidgets
class Array:

    def __init__(self, tipoDato, identificador, listaExpresiones):
        self.tipoDato = tipoDato
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def __repr__(self):
        return "(Arreglo: tipoDato: %s, identificador: %s, listaExpresiones: %s)" % (self.tipoDato, self.identificador, self.listaExpresiones)

    def __str__(self):
        return "Arreglo [ %s, %s, %s]"% (self.tipoDato, self.identificador, self.listaExpresiones)
    
    def construirArbol(self, arbol):
        arbol.setText(0,"Arreglo")
        ramaCadena = QtWidgets.QTreeWidgetItem(arbol)
        ramaCadena.setText(0,"identificador "+self.identificador.lexema)
        ramaCadena = QtWidgets.QTreeWidgetItem(arbol)
        ramaCadena.setText(0,"Tipo Dato "+self.tipoDato.lexema)

        ramaElementos = QtWidgets.QTreeWidgetItem(arbol)
        ramaElementos.setText(0,"Elementos ")
        
        if len(self.listaExpresiones) >0:
            for exp in self.listaExpresiones:
                arbolExpresion = QtWidgets.QTreeWidgetItem(ramaElementos)
                exp.construirArbol(arbolExpresion)

    