from logica.sintactico.Expresion import Expression
from PyQt5 import QtWidgets

class Relacional(Expression):

    def __init__(self, expRelacional, expAuxiliarRelacional, termino):
        self.expresionRelacional = expRelacional
        self.expresionAuxiliarRelacional = expAuxiliarRelacional
        self.termino = termino

    def construirArbol(self, arbol):
        #Los arboles en realidad son nodos de partida o raices
        #llega el 'arbol' nodo 'R'
               
        if self.expresionAuxiliarRelacional != None:                          #Si hay una expr Auxiliar
            
            self.expresionAuxiliarRelacional.construirArbol(arbol)            #Llamamos el mtodo crear arbol de aux
            
            if self.termino != None:                                #Si hay un termino
                term = QtWidgets.QTreeWidgetItem(arbol)             #Sacamos un hijo 'A' de 'R' 
                term.setText(0,self.termino.lexema)                 #le asignamos a 'A' el termino
                
            elif self.expresionRelacional != None:                  #Sino, si hay expresion relaciona
                arbolExp = QtWidgets.QTreeWidgetItem(arbol)         #Sacamos un hijo 'B' de R
                self.expresionRelacional.construirArbol(arbolExp)   #en 'B' hacemos la raiz del arbol de ExpresionAritmetica
        
        
        else:                                                       #Sino hay una expresion auxiliar(mas facil)
            
            if self.termino != None:                                #Si hay un termino                                
                arbol.setText(0, self.termino.lexema)               #nombremos 'R' como el termino
        
           
            elif self.expresionRelacional != None:                  #Sino, si hay una expresion Aritmetica
                self.expresionRelacional.construirArbol(arbol)      #hacemos 'R' la raiz del nuevo arbol de expresion aritmetica    
    

    def __repr__(self):
        return "(Expresion relaciona:  %s eAuxArit:: %s termino: %s)" % (self.expresionRelacional, self.expresionAuxiliarRelacional, self.termino)

    def __str__(self):
        return "ExpresionRelaciona:  %s eAuxArit:: %s termino: %s)" % (self.expresionRelacional, self.expresionAuxiliarRelacional, self.termino)
    