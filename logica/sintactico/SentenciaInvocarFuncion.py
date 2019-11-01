from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <InvocarMetodo>::= invocar identificador "("[<ListaArgumentos>]")" ";"
"""
class InvocarFuncion(Sentence):

    def __init__(self, identificador, listaArgumentos):
        self.identificador = identificador
        self.listaArgumentos = listaArgumentos

    def __repr__(self):
        return "(Sentencia Invocar Funcion: identificador: %s, listaArgumentos: %s)" % (self.identificador, self.listaArgumentos)

    def __str__(self):
        return "Sentencia Invocar Funcion [%s, %s]"% (self.identificador, self.listaArgumentos)
    
    def construirArbol(self, arbol):
        arbolInvocarFuncion = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "InvocarFuncion "
        arbolInvocarFuncion.setText(0,titulo)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolInvocarFuncion)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

        
        if len(self.listaArgumentos) > 0:
            ramaListaArgumentos = QtWidgets.QTreeWidgetItem(arbolInvocarFuncion)
            ramaListaArgumentos.setText(0,"Argumentos ")
            cont = 0
            
            for argumento in self.listaArgumentos:
                argumento.construirArbol(ramaListaArgumentos, cont)
                cont += 1
