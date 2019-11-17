from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
from logica.lexico.Categorias import Categoria
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
    
    def analisisSemantico(self,tablaSimbolos,listaErrores):
        for simbolo in tablaSimbolos.listaSimbolos:
            if simbolo.nombre == self.identificador.lexema:
                print("Existe la variable en tabla ahora va a buscar la exp "+str(self.expresion))
                self.expresion.analisisSemantico(tablaSimbolos,listaErrores)
                self.analisisTipoDato(simbolo,listaErrores)
                return True
        err = "La variable \""+self.identificador.lexema+"\" no se encuentra declarada."
        listaErrores.append(err)

    def analisisTipoDato(self,simbolo,listaErrores):
        tipoDatoExpresion = self.expresion.obtenerTipoDato()
        print("El tipo de dato es ",tipoDatoExpresion,"  ",simbolo.tipoDato )
        if tipoDatoExpresion == Categoria.NumeroNatural:
            if simbolo.tipoDato.lexema == 'int':
                return True
            else:
                err = "La variable \""+self.identificador.lexema+"\" no se le asigno un tipo de dato valido, asigne un "+simbolo.tipoDato.lexema
                listaErrores.append(err)
                return False
        elif tipoDatoExpresion == Categoria.NumeroReal:
            if simbolo.tipoDato.lexema == 'double':
                return True
            else:
                err = "La variable \""+self.identificador.lexema+"\" no se le asigno un tipo de dato valido, asigne un "+simbolo.tipoDato.lexema
                listaErrores.append(err)
                return False
        elif tipoDatoExpresion == Categoria.OperadorLogico:
            if simbolo.tipoDato.lexema == 'boolean':
                return True
            else:
                err = "La variable \""+self.identificador.lexema+"\" no se le asigno un tipo de dato valido, asigne un "+simbolo.tipoDato.lexema
                listaErrores.append(err)
                return False
        elif tipoDatoExpresion == Categoria.CadenaCaracteres:
            if simbolo.tipoDato.lexema == 'String':
                return True
            else:
                err = "La variable \""+self.identificador.lexema+"\" no se le asigno un tipo de dato valido, asigne un "+simbolo.tipoDato.lexema
                listaErrores.append(err)
                return False

        
        print("Es otro tipo de dato")


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

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    