from logica.sintactico.Expresion import Expression
from PyQt5 import QtWidgets
class AuxiliarRelacional(Expression):
    
    def __init__(self,operadorRelacional, expresionRelacional, expresionAuxiliarRelacional):
        
        self.operadorRelacional = operadorRelacional
        self.expresionRelacional = expresionRelacional
        self.expresionAuxiliar = expresionAuxiliarRelacional
    
    def construirArbol(self, arbol):
        #Los arboles en realidad son nodos de partida o raices
        #llega el 'arbol' nodo 'F'
                                                                    #nada mas llega F, le asignamos                        
        arbol.setText(0, self.operadorRelacional.lexema)            #como titulo el operador
        arbolExp = QtWidgets.QTreeWidgetItem(arbol)                 #Se crea un nodo 'K' a partir de 
                                                                    #ese operador 'F'
        
        if self.expresionAuxiliar != None :                         #Si hay una expresion auxiliar dentro,

            self.expresionAuxiliar.construirArbol(arbolExp)         #Se llama el metodo constArbol de auxiliar
                                                                    #es decir, este mismo, para que ponga el    
                                                                    #operador, en el nodo 'K' etc             
 
            arbolExpAux = QtWidgets.QTreeWidgetItem(arbolExp)       #Se crea un nodo 'T' con raiz en 'K'       
            self.expresionRelacional.construirArbol(arbolExpAux)    #Crece el arbol expAritm con raiz en 'T'
        else:
                                                                    #Si ninguna de estas locuras se cumplen
            self.expresionRelacional.construirArbol(arbolExp)       #Crece el arbol expAritm con raiz en 'K'
    

    def __repr__(self):
        return "(Expresion Auxiliar Relacional:  Operador%s eArit:: %s eAuxArit: %s)" % (self.operadorRelacional, self.expresionRelacional, self.expresionAuxiliar)

    def __str__(self):
        return "(Expresion Auxiliar Relacional:  Operador%s eArit:: %s eAuxArit: %s)" % (self.operadorRelacional, self.expresionRelacional, self.expresionAuxiliar)

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    