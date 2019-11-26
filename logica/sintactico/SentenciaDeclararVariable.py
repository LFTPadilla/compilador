from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
from logica.lexico.Categorias import Categoria
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
        tablaSimbolos.guardarSimboloVariable(self.identificador , self.tipoDato,self.tipoDato.fila,self.tipoDato.columna, ambito, self.expresion)

    def analisisSemantico(self,tablaSimbolos,listaErrores):
                  
        if self.expresion != None:
            self.expresion.analisisSemantico(tablaSimbolos,listaErrores,self.tipoDato)
            self.analisisTipoDato(listaErrores)
            return True
        if self.invocacion !=None:
            self.invocacion.analisisSemantico(tablaSimbolos,listaErrores)
            
            return True
        if self.lectura !=None:
            self.lectura.analisisSemantico(tablaSimbolos,listaErrores)
            return True
        
    def obtenerPythonCode(self):

    def analisisTipoDato(self,listaErrores):
        tipoDatoExpresion = self.expresion.obtenerTipoDato()
        print("El tipo de dato es ",tipoDatoExpresion,"  ",self.tipoDato )
        if tipoDatoExpresion == Categoria.NumeroNatural:
            if self.tipoDato.lexema == 'int':
                return True
            else:
                err = "La variable \""+self.identificador.lexema+"\" no se le asigno un tipo de dato valido, asigne un "+self.tipoDato.lexema
                listaErrores.append(err)
                return False
        elif tipoDatoExpresion == Categoria.NumeroReal:
            if self.tipoDato.lexema == 'double':
                return True
            else:
                err = "La variable \""+self.identificador.lexema+"\" no se le asigno un tipo de dato valido, asigne un "+self.tipoDato.lexema
                listaErrores.append(err)
                return False
        elif tipoDatoExpresion == Categoria.OperadorLogico:
            if self.tipoDato.lexema == 'boolean':
                return True
            else:
                err = "La variable \""+self.identificador.lexema+"\" no se le asigno un tipo de dato valido, asigne un "+self.tipoDato.lexema
                listaErrores.append(err)
                return False
        elif tipoDatoExpresion == Categoria.CadenaCaracteres:
            if self.tipoDato.lexema == 'String':
                return True
            else:
                err = "La variable \""+self.identificador.lexema+"\" no se le asigno un tipo de dato valido, asigne un "+self.tipoDato.lexema
                listaErrores.append(err)
                return False

        
        print("NO esta configurado el tipo de dato que recibió")
        
