from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression
"""
    <ExpresionCadena>::= cadena [ "+" <Expresion> ] 
"""
class Cadena(Expression):

    def __init__(self, cadenaCaracteres, listarExpresiones):
        self.cadenaCaracteres = cadenaCaracteres
        self.listarExpresiones =  listarExpresiones

    def construirArbol(self, arbolExpresionCadena):
        arbolExpresionCadena.setText(0,"Cadena")
        ramaCadena = QtWidgets.QTreeWidgetItem(arbolExpresionCadena)
        ramaCadena.setText(0,self.cadenaCaracteres.lexema)


        if len(self.listarExpresiones) >0:
        
                         
            for exp in  self.listarExpresiones:
                arbolExpresion = QtWidgets.QTreeWidgetItem(arbolExpresionCadena)
                exp.construirArbol(arbolExpresion)

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    
            
