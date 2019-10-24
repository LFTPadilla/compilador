from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression

class Aritmetica(Expression):

    def __init__(self, expAritmetica, expAuxiliarAritmetica, termino):
        self.expresionAritmetica = expAritmetica
        self.expresionAuxiliar = expAuxiliarAritmetica
        self.termino = termino

    def construirArbol(self, arbol):
        
               
        if self.expresionAuxiliar != None: 
            print("Hay auxiliar Grfica")
            self.expresionAuxiliar.construirArbol(arbol)
            
            if self.termino != None:
                term = QtWidgets.QTreeWidgetItem(arbol)
                term.setText(0,self.termino.lexema)
            elif self.expresionAritmetica != None:
                arbolExp = QtWidgets.QTreeWidgetItem(arbol)
                self.expresionAritmetica.construirArbol(arbolExp)
        
        else:
            if self.termino != None:
                print ("termino")
                arbol.setText(0, self.termino.lexema)
        
           
            elif self.expresionAritmetica != None:  
                print ("-------------------Hay expresion aritmetica", (str)(self.expresionAritmetica))
                self.expresionAritmetica.construirArbol(arbol)          
            
      
    def __repr__(self):
        return "(Expresion Aritmetica: Expresion aritmetica: %s eAuxArit:: %s termino: %s)" % (self.expresionAritmetica, self.expresionAuxiliar, self.termino)

    def __str__(self):
        return "ExpresionAritmetica: Expresion aritmetica: %s eAuxArit:: %s termino: %s)" % (self.expresionAritmetica, self.expresionAuxiliar, self.termino)
    
        
           
            
