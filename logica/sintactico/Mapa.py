from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <Mapa>::= map identificador "=" <listaComponentesMap>
"""
class mapita(Sentence):

    def __init__(self, identificador, listaComponentes):
        self.identificador = identificador
        self.listaComponentes = listaComponentes

    def __repr__(self):
        return "(Mapa: identificador: %s listaComponentes: %s)" % (self.identificador, self.listaComponentes)

    def __str__(self):
        return "Mapa [%s, %s]" % (self.identificador, self.listaComponentes)
    
    def construirArbol(self, arbol):
        arbolMapa = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "Map "
        arbolMapa.setText(0,titulo)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolMapa)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

        ramaListaComponentes = QtWidgets.QTreeWidgetItem(arbolMapa)
        ramaListaComponentes.setText(0,"ListaComponentesMapa")
        cont = 0

        for componentesMapa in self.listaComponentes:
            componentesMapa.construirArbol(ramaListaComponentes, cont)
            cont += 1

        