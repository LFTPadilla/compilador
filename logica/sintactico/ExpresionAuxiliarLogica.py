from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression

"""
    <ExpresionAuxiliarLogica>::= operadorLogico ["!"] <ExpresionLogica>
"""

class AuxiliarLogica(Expression):
    
    def __init__(self, operadorLogico, expresionLogica, expresionAuxLogica):
        self.operadorLogico = operadorLogico
        self.expresionLogica = expresionLogica
        self.expresionAuxLogica = expresionAuxLogica
    
    def construirArbol(self, arbol):

        #Los arboles en realidad son nodos de partida o raices
        #llega el 'arbol' nodo 'F'
                                                                    #nada mas llega F, le asignamos                        
        arbol.setText(0, self.operadorLogico.lexema)            #como titulo el operador
        
        arbolExp = QtWidgets.QTreeWidgetItem(arbol)                 #Se crea un nodo 'K' a partir de 
                                                                    #ese operador 'F'
        
        if self.expresionAuxLogica != None :                         #Si hay una expresion auxiliar dentro,

            self.expresionAuxLogica.construirArbol(arbolExp)         #Se llama el metodo constArbol de auxiliar
                                                                     #es decir, este mismo, para que ponga el    
                                                                     #operador, en el nodo 'K' etc             
            arbolExpAux = QtWidgets.QTreeWidgetItem(arbolExp)       #Se crea un nodo 'T' con raiz en 'K'       
            self.expresionLogica.construirArbol(arbolExpAux)    #Crece el arbol expLogica con raiz en 'T'

            
        else:
                                                                    #Si ninguna de estas locuras se cumplen
            self.expresionLogica.construirArbol(arbolExp)       #Crece el arbol expLogica con raiz en 'K'
            
        
       
        