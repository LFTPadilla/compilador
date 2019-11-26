from PyQt5 import QtWidgets
from logica.sintactico.Expresion import Expression
from logica.lexico.Categorias import Categoria


"""
<ExpresionCadena>::= cadena [ "," <listaExpresiones> ] 
"""
class Cadena(Expression):

    def __init__(self, cadenaCaracteres, listarExpresiones):
        self.cadenaCaracteres = cadenaCaracteres
        self.listarExpresiones =  listarExpresiones

    def analisisSemantico(self,tablaSimbolos,listaErrores,tipoDato):
        
        if len(self.listarExpresiones)>0:
            for exp in self.listarExpresiones:
                exp.analisisSemantico(tablaSimbolos,listaErrores)

    def obtenerTipoDato(self):
        return Categoria.CadenaCaracteres


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
    
            
