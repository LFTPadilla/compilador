from PyQt5 import QtWidgets
"""
    <IncrementoDecremento>::=  identificador ++ ";" |    identificador -- ";" 
"""

class IncrementoDecremento:

    def __init__(self, identificador,operadorIncDec):
        self.identificador = identificador
        self.operadorIncDec = operadorIncDec

    def __repr__(self):
        return "(identificador: %s, Operador %s)" % (self.identificador,self.operadorIncDec)

    def __str__(self):
        return "(identificador: %s, Operador %s)" % (self.identificador,self.operadorIncDec)
                
    def construirArbol(self, arbol):
        arbol = QtWidgets.QTreeWidgetItem(arbol)
        
        if self.operadorIncDec.lexema == "++":
            titulo = "Incremento "
            arbol.setText(0,titulo)
        else:
            titulo = "Decremento "
            arbol.setText(0,titulo)
        
        ramaIdent = QtWidgets.QTreeWidgetItem(arbol)
        ramaIdent.setText(0,"Identificador "+self.identificador.lexema)

        ramaOp = QtWidgets.QTreeWidgetItem(arbol)
        ramaOp.setText(0,"Operador "+self.operadorIncDec.lexema)
