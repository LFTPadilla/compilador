from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
from logica.lexico.Categorias import Categoria

"""
    <Retorno>::= return <Expresion> ";"
"""
class Retorno(Sentence):

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Retorno: expresion: %s)" % (self.expresion)

    def __str__(self):
        return "Sentencia Retorno [%s]"% (self.expresion)
    
    def construirArbol(self, arbol):
        arbolRetorno = QtWidgets.QTreeWidgetItem(arbol)
        arbolRetorno.setText(0,"Return")

        ramaExpresion = QtWidgets.QTreeWidgetItem(arbolRetorno)
        ramaExpresion.setText(0,"Expresion ")
            
        arbolExpresion = QtWidgets.QTreeWidgetItem(ramaExpresion)            
        self.expresion.construirArbol(arbolExpresion)
    

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    def analisisSemantico(self,tablaSimbolos,listaErrores, ambito ):
        
        funcion = None
        #capturamos el simbolo con ese ambito(ambito = nombre de la funcion contenedora del return)
        for simbolo in tablaSimbolos.listaSimbolos:
            if simbolo.tipoRetorno != None:
                
                if simbolo.nombre == ambito:
                    
                    funcion = simbolo
                    break
        print("SERA CHAR?_______/////////////////////_________:",len(self.expresion.cadenaCaracteres.lexema))
                    
        if funcion.tipoRetorno == "int" and self.expresion.obtenerTipoDato() == Categoria.NumeroNatural :
            print("Funcion de tipo int y expresion de retorno numero natural")
            return True
        elif funcion.tipoRetorno == "double" and self.expresion.obtenerTipoDato() == Categoria.NumeroReal :
            print("Funcion de tipo double y expresion de retorno numero real")
            
            return True
         #se compara el tamanio de la cadena con 3 porque hay 2 comillas y 1 caracter en el lexema
        elif funcion.tipoRetorno == "char" and self.expresion.obtenerTipoDato() == Categoria.CadenaCaracteres and len(self.expresion.cadenaCaracteres.lexema) == 3:
            print("Funcion de tipo char y expresion de retorno char")
            
            return True
        elif funcion.tipoRetorno == "String" and self.expresion.obtenerTipoDato() == Categoria.CadenaCaracteres :
            print("Funcion de tipo String y expresion de retorno cadena")
            
            return True
       
        elif funcion.tipoRetorno == "boolean" and self.expresion.obtenerTipoDato() == Categoria.OperadorLogico :
            print("Funcion de tipo boolean y expresion de retorno bool")
            
            return True
        elif funcion.tipoRetorno == "void":
            listaErrores.append("No puede haber un retorno dentro de una funcion void")
       
        else: 
            listaErrores.append("Tipo de retorno no valido en la funcion "+str(ambito))
            
                    
             