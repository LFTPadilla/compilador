from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <DeclaracionVariable>::= <tipoDato> identificador [ "=" <lectura> | "=" <invocacion> |  "=" <Expresion> ]  ";"
"""
class DeclaracionVariable(Sentence):

    def __init__(self,tipoDato, identificador, lectura, invocacion, expresion):
        self.tipoDato = tipoDato
        self.identificador = identificador
        self.lectura = lectura
        self.invocacion = invocacion
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Declaracion Variable: tipoDato: %s, identificador: %s, lectura: %s, invocacion: %s, expresion: %s)" % (self.tipoDato, self.identificador, self.lectura, self.invocacion, self.expresion)

    def __str__(self):
        return "[Sentencia Declaracion Variable [%s, %s, %s, %s, %s]"% (self.tipoDato, self.identificador, self.lectura, self.invocacion, self.expresion)
    
    def construirArbol(self, arbol, n):
        arbolDeclaracionVariable = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "DeclaracionVariable "+str(n)
        arbolDeclaracionVariable.setText(0,titulo)

        ramaTipoDato = QtWidgets.QTreeWidgetItem(arbolDeclaracionVariable)
        ramaTipoDato.setText(0,"TipoDato "+self.tipoDato.lexema)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolDeclaracionVariable)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

        if self.lectura != None:
            self.lectura.construirArbol(arbolDeclaracionVariable, 0)        

        if self.invocacion != None:
            self.invocacion.construirArbol(arbolDeclaracionVariable, 0)

        if self.expresion != None:
           self.expresion.construirArbol(arbolDeclaracionVariable)
