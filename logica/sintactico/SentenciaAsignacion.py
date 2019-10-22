from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <AsignacionVariable>::= identificador operadorAsignacion <expresion> ";"
"""
class Asignacion(Sentence):

    def __init__(self, identificador, operadorAsignacion, expresion):
        self.identificador = identificador
        self.operadorAsignacion = operadorAsignacion
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Asignacion: identificador: %s,operadorAsignacion: %s, expresion: %s)" % (self.identificador, self.operadorAsignacion, self.expresion)

    def __str__(self):
        return "Sentencia Asignacion [%s, %s, %s]"% (self.identificador, self.operadorAsignacion, self.expresion)
    
    def construirArbol(self, arbol, n):
        arbolAsignacionVariable = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "AsignacionVariable "+str(n)
        arbolAsignacionVariable.setText(0,titulo)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolAsignacionVariable)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

        ramaOperadorAsignacion = QtWidgets.QTreeWidgetItem(arbolAsignacionVariable)
        ramaOperadorAsignacion.setText(0,"OperadorAsignacion "+self.operadorAsignacion.lexema)

        #self.expresion.construirArbol(arbolAsignacionVariable)