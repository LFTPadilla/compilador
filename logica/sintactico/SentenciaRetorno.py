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
                print("El simbolo es una funcion---------------------------------")
                print("Simbolo.nombre: ",simbolo.nombre)
                print("Ambito: ",ambito)
                
                if simbolo.nombre == ambito:
                    print("Encontrada",ambito,"---------------------------------")
                    
                    funcion = simbolo
                    break
        print("Holalola")
        print(funcion)
       
        if funcion.tipoRetorno == "int" and self.expresion.categoria == Categoria.NumeroNatural :
            print("Funcion de tipo int expresion de retorno numero natural")
            return True
        elif funcion.tipoRetorno == "double" and self.expresion.categoria == Categoria.NumeroReal :
            print("Funcion de tipo double expresion de retorno numero real")
            
            return True
        else: 
            listaErrores.append("Tipo de retorno no valido en la funcion",ambito)
            
                    
             