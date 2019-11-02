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
    
    def construirArbol(self, arbol):
        arbolDeclaracionVariable = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "DeclaracionVariable "
        arbolDeclaracionVariable.setText(0,titulo)

        ramaTipoDato = QtWidgets.QTreeWidgetItem(arbolDeclaracionVariable)
        ramaTipoDato.setText(0,"TipoDato "+self.tipoDato.lexema)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolDeclaracionVariable)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

        if self.lectura != None:
            self.lectura.construirArbol(arbolDeclaracionVariable)        

        if self.invocacion != None:
            self.invocacion.construirArbol(arbolDeclaracionVariable)

        if self.expresion != None:
            ramaExpresion = QtWidgets.QTreeWidgetItem(arbolDeclaracionVariable)
            ramaExpresion.setText(0,"Expresion ")
            
            arbolExpresion = QtWidgets.QTreeWidgetItem(ramaExpresion)            
            self.expresion.construirArbol(arbolExpresion)


    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos,ambito):
        tablaSimbolos.guardarSimboloVariable(self.identificador, self.tipoDato, ambito, self.expresion)

    def analizarSemantica(self,tablaSimbolos, erroresSemanticos, simbolo):

        simbolo1 =  tablaSimbolos.buscarSimboloVariable (self.identificador.lexema, "", self.identificador )
        if simbolo1 ==None:
            erroresSemanticos.add("No existe la variable ", self.identificador.lexema)
        
