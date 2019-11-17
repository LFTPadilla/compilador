from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression
from logica.lexico.Categorias import Categoria

class Aritmetica(Expression):

    def __init__(self, expAritmetica, expAuxiliarAritmetica, termino):
        self.expresionAritmetica = expAritmetica
        self.expresionAuxiliar = expAuxiliarAritmetica
        self.termino = termino

    def obtenerTipoDato(self):

        tipo = None
        if self.termino!=None:
            tipo = self.termino.categoria
        if self.expresionAuxiliar != None:
            tipo2 = self.expresionAuxiliar.obtenerTipoDato()
            if tipo == Categoria.NumeroReal:
                return tipo
            else:
                return tipo2
        else:
            return tipo

    def analisisSemantico(self,tablaSimbolos,listaErrores):
        print("Entro al analisis semantico exp aritmetica ",self.termino)
        if self.termino!=None and self.termino.categoria == Categoria.Identificador:
            for simbolo in tablaSimbolos.listaSimbolos:
                if simbolo.nombre == self.termino.lexema:
                    if self.expresionAuxiliar!=None:
                        print("Entro a analizar exp aux")
                        self.expresionAuxiliar.analisisSemantico(tablaSimbolos,listaErrores)
                    return True
            if self.expresionAuxiliar!=None:
                print("Entro a analizar exp aux")
                self.expresionAuxiliar.analisisSemantico(tablaSimbolos,listaErrores)
            err = "La variable \""+self.termino.lexema+"\" no se encuentra declarada."
            print("err "+err)
            listaErrores.append(err)
        else:
            print("El termino no es un ident continuara con ",self.expresionAritmetica,"   yyy  con  ",self.expresionAuxiliar)
            if self.expresionAritmetica!=None:
                self.expresionAritmetica.analisisSemantico(tablaSimbolos,listaErrores)
            if self.expresionAuxiliar!=None:
                print("Entro a analizar exp aux")
                self.expresionAuxiliar.analisisSemantico(tablaSimbolos,listaErrores)
            return True


    def construirArbol(self, arbol):
        #Los arboles en realidad son nodos de partida o raices
        #llega el 'arbol' nodo 'R'
               
        if self.expresionAuxiliar != None:                          #Si hay una expr Auxiliar
            
            self.expresionAuxiliar.construirArbol(arbol)            #Llamamos el mtodo crear arbol de aux
            
            if self.termino != None:                                #Si hay un termino
                term = QtWidgets.QTreeWidgetItem(arbol)             #Sacamos un hijo 'A' de 'R' 
                term.setText(0,self.termino.lexema)                 #le asignamos a 'A' el termino
                
            elif self.expresionAritmetica != None:                  #Sino, si hay expresion Aritmetica
                arbolExp = QtWidgets.QTreeWidgetItem(arbol)         #Sacamos un hijo 'B' de R
                self.expresionAritmetica.construirArbol(arbolExp)   #en 'B' hacemos la raiz del arbol de ExpresionAritmetica
        
        
        else:                                                       #Sino hay una expresion auxiliar(mas facil)
            
            if self.termino != None:                                #Si hay un termino                                
                arbol.setText(0, self.termino.lexema)               #nombremos 'R' como el termino
        
           
            elif self.expresionAritmetica != None:                  #Sino, si hay una expresion Aritmetica
                self.expresionAritmetica.construirArbol(arbol)      #hacemos 'R' la raiz del nuevo arbol de expresion aritmetica    
            
      
    def __repr__(self):
        return "(Expresion Aritmetica: Expresion aritmetica: %s eAuxArit:: %s termino: %s)" % (self.expresionAritmetica, self.expresionAuxiliar, self.termino)

    def __str__(self):
        return "ExpresionAritmetica: Expresion aritmetica: %s eAuxArit:: %s termino: %s)" % (self.expresionAritmetica, self.expresionAuxiliar, self.termino)
    

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    
           
            
