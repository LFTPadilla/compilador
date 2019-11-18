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

        if self.expresion != None:
            ramaExpresion = QtWidgets.QTreeWidgetItem(arbolAsignacionVariable)
            ramaExpresion.setText(0,"Expresion ")

            arbolExpresion = QtWidgets.QTreeWidgetItem(ramaExpresion)
            self.expresion.construirArbol(arbolExpresion)
    def obtenerPythonCode(self):
        codigo = ""
        if self.lectura != None and self.invocacion == None and self.expresion == None:
            codigo = self.identificador.obtenerPythonCode() + " " + self.operadorAsignacion.obtenerPythonCode() + " " + self.lectura.obtenerPythonCode() + ";"
        elif self.invocacion != None and self.lectura == None and self.expresion == None:
            codigo = self.identificador.obtenerPythonCode() + " " + self.operadorAsignacion.obtenerPythonCode() + " " + self.invocacion.obtenerPythonCode() + ";"
        elif self.expresion != None and self.invocacion == None and self.lectura == None:
            codigo = self.identificador.obtenerPythonCode() + " " + self.operadorAsignacion.obtenerPythonCode() + " " + self.expresion.obtenerPythonCode() + ";"
        return codigo

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    