from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression


class AuxiliarAritmetica(Expression):
    
    def __init__(self,operadorAritmetico, expresionAritmetica, expresionAuxiliarAritmetica):
        
        self.operadorAritmetico = operadorAritmetico
        self.expresionAritmetica = expresionAritmetica
        self.expresionAuxiliar = expresionAuxiliarAritmetica
    
    def analisisSemantico(self,tablaSimbolos,listaErrores):
        print("Analizar exp aux ",self.expresionAuxiliar)
        print("Analizar exp ",self.expresionAritmetica)
        if self.expresionAuxiliar!=None:
            self.expresionAuxiliar.analisisSemantico(tablaSimbolos,listaErrores)
        if self.expresionAritmetica!=None:
            self.expresionAritmetica.analisisSemantico(tablaSimbolos,listaErrores)
        
    def obtenerTipoDato(self):
        return self.expresionAritmetica.obtenerTipoDato()

    def construirArbol(self, arbol):
        #Los arboles en realidad son nodos de partida o raices
        #llega el 'arbol' nodo 'F'
                                                                    #nada mas llega F, le asignamos                        
        arbol.setText(0, self.operadorAritmetico.lexema)            #como titulo el operador
        
        arbolExp = QtWidgets.QTreeWidgetItem(arbol)                 #Se crea un nodo 'K' a partir de 
                                                                    #ese operador 'F'
        
        if self.expresionAuxiliar != None :                         #Si hay una expresion auxiliar dentro,

            self.expresionAuxiliar.construirArbol(arbolExp)         #Se llama el metodo constArbol de auxiliar
                                                                    #es decir, este mismo, para que ponga el    
                                                                    #operador, en el nodo 'K' etc             
 
            arbolExpAux = QtWidgets.QTreeWidgetItem(arbolExp)       #Se crea un nodo 'T' con raiz en 'K'       
            self.expresionAritmetica.construirArbol(arbolExpAux)    #Crece el arbol expAritm con raiz en 'T'
        else:
                                                                    #Si ninguna de estas locuras se cumplen
            self.expresionAritmetica.construirArbol(arbolExp)       #Crece el arbol expAritm con raiz en 'K'
            
            
                
    def __repr__(self):
        return "(Expresion Auxiliar Aritmetica:  Operador%s eArit:: %s eAuxArit: %s)" % (self.operadorAritmetico, self.expresionAritmetica, self.expresionAuxiliar)

    def __str__(self):
        return "(Expresion Auxiliar Aritmetica:  Operador%s eArit:: %s eAuxArit: %s)" % (self.operadorAritmetico, self.expresionAritmetica, self.expresionAuxiliar)
        

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    
             
        
        
        