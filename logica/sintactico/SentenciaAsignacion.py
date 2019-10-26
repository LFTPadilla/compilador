from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <AsignacionVariable>::= identificador operadorAsignacion <expresion> ";" | identificador operadorAsignacion <Lectura> ";" | identificador operadorAsignacion <invocacion> ";"
"""
class Asignacion(Sentence):

    def __init__(self, identificador, operadorAsignacion, lectura, invocacion, expresion):
        self.identificador = identificador
        self.operadorAsignacion = operadorAsignacion
        self.lectura = lectura
        self.invocacion = invocacion
        self.expresion = expresion

    def __repr__(self):
        return "(Asignacion Variable: identificador: %s, operadorAsignacion: %s, lectura: %s, invocacion: %s, expresion: %s)" % (self.identificador, self.operadorAsignacion, self.lectura, self.invocacion, self.expresion)

    def __str__(self):
        return "[asignacion Variable [%s, %s, %s, %s, %s]"% (self.identificador,self.operadorAsignacion, self.lectura, self.invocacion, self.expresion)
    
    def construirArbol(self, arbol):
        arbolAsignacionVariable = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "AsignacionVariable "
        arbolAsignacionVariable.setText(0,titulo)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolAsignacionVariable)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

        ramaOperadorAsignacion = QtWidgets.QTreeWidgetItem(arbolAsignacionVariable)
        ramaOperadorAsignacion.setText(0,"OperadorAsignacion "+self.operadorAsignacion.lexema)

        if self.lectura != None:
            self.lectura.construirArbol(arbolAsignacionVariable)        

        if self.invocacion != None:
            self.invocacion.construirArbol(arbolAsignacionVariable)

        #if self.expresion != None:
        #    self.expresion.construirArbol(arbol)