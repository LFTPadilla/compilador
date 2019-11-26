from logica.sintactico.Expresion import Expression
from PyQt5 import QtWidgets
from logica.lexico.Categorias import Categoria

class Relacional(Expression):

    def __init__(self, expresionAritmetica1,operadorRelacional, expresionAritmetica2):
        self.expresionAritmetica1 = expresionAritmetica1
        self.operadorRelacional = operadorRelacional
        self.expresionAritmetica2 = expresionAritmetica2

    def analisisSemantico(self,tablaSimbolos,listaErrores,tipoDato):
        print("Entro al analisis semantico relacional ",self.expresionAritmetica1)
        self.expresionAritmetica1.analisisSemantico(tablaSimbolos,listaErrores,tipoDato)
        self.expresionAritmetica2.analisisSemantico(tablaSimbolos,listaErrores,tipoDato)


    def obtenerPythonCode(self):
        codigo =  self.expresionAritmetica1.obtenerPythonCode() + self.operadorRelacional.lexema +    self.expresionAritmetica2.obtenerPythonCode()
        return codigo

    def construirArbol(self, arbol):
        #Los arboles en realidad son nodos de partida o raices
        #llega el 'arbol' nodo 'R'

        if self.operadorRelacional != None :
            arbol.setText(0,self.operadorRelacional.lexema)

            ramaExpresion1 = QtWidgets.QTreeWidgetItem(arbol)
            self.expresionAritmetica1.construirArbol(ramaExpresion1)
            
            ramaExpresion2 = QtWidgets.QTreeWidgetItem(arbol)
            self.expresionAritmetica2.construirArbol(ramaExpresion2)
            
        elif self.expresionAritmetica1 != None and self.operadorRelacional == None:            
            self.expresionAritmetica1.construirArbol(arbol)

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    