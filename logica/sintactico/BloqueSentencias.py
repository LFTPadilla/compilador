from PyQt5 import QtWidgets
"""
        <BloqueSentencia> ::= "{" [<listaSentencias>] "}"
"""
class bloqueSent:
    
    def __init__(self, listaSentencias):
        self.listaSentencias = listaSentencias

    def __repr__(self):
        return "(BloqueSentencias: listaSentencias: %s)" % (self.listaSentencias)

    def __str__(self):
        return "BloqueSentencias [%s]" % ( self.listaSentencias)

    def construirArbol(self, arbol):
        arbolBloque = QtWidgets.QTreeWidgetItem(arbol)
        arbolBloque.setText(0,"Bloque Sentencias")

        if len(self.listaSentencias) > 0:
            ramaListaSent = QtWidgets.QTreeWidgetItem(arbolBloque)
            ramaListaSent.setText(0,"listaSentencias")

            
            for sentencia in self.listaSentencias:
                sentencia.construirArbol(ramaListaSent)

