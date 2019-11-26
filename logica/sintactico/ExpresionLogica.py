from PyQt5 import QtWidgets

from logica.sintactico.Expresion import Expression
from logica.lexico.Categorias import Categoria

"""
    <ExpresionLogica>::=    
    "!" "(" <ExpresionLogica> ")" [operadorLogico <ExpresionLogica>] [<ExpresionAuxiliarLogica>]
    | "(" <ExpresionLogica> operadorLogicoBinario <ExpresionLogica> ")" operadorLogicoBinario <ExpresionLogica> [<ExpresionAuxiliarLogica>] 
    | <ExpresionRelacional> [<ExpresionAuxiliarLogica>]                         
"""
class Logica(Expression):

    def __init__(self, operador1, expresionLogica1, operador2, expresionLogica2, expresionLogica3, expresionRelacional, expresionAuxiliarLogica):
        self.operador1 = operador1
        self.expresionLogica1 = expresionLogica1
        self.operador2 = operador2
        self.expresionLogica2 = expresionLogica2
        self.expresionLogica3 = expresionLogica3
        self.expresionRelacional = expresionRelacional
        self.expresionAuxiliarLogica = expresionAuxiliarLogica
    

    def obtenerPythonCode(self):
        codigo = ""
        
            
        return codigo

    def analisisSemantico(self,tablaSimbolos,listaErrores,tipoDato):
        if self.expresionRelacional !=None:
            self.expresionRelacional.analisisSemantico(tablaSimbolos,listaErrores,tipoDato)
        if self.expresionLogica1 != None:
            self.expresionLogica1.analisisSemantico(tablaSimbolos,listaErrores,tipoDato)
        if self.expresionLogica2 != None:
            self.expresionLogica2.analisisSemantico(tablaSimbolos,listaErrores,tipoDato)
        if self.expresionLogica3 != None:
            self.expresionLogica3.analisisSemantico(tablaSimbolos,listaErrores,tipoDato)
        if self.expresionAuxiliarLogica != None:
            self.expresionAuxiliarLogica.analisisSemantico(tablaSimbolos,listaErrores,tipoDato)
    
    def obtenerTipoDato(self):
        return Categoria.OperadorLogico

    def construirArbol(self, arbol):
       
        if self.expresionRelacional != None:
                     
            if self.expresionAuxiliarLogica != None:
                self.expresionAuxiliarLogica.construirArbol(arbol)                             
                nodoOperadorAux = QtWidgets.QTreeWidgetItem(arbol)
                self.expresionRelacional.construirArbol(nodoOperadorAux)
            else:
                self.expresionRelacional.construirArbol(arbol)        
    
        if self.operador2 != None:
            arbol.setText(0, self.operador2.lexema)
        
            if self.operador1 != None and self.operador1.lexema == "!":
                nodoNegacion = QtWidgets.QTreeWidgetItem(arbol)
                nodoNegacion.setText(0, self.operador1.lexema)
                ramaNegacion = QtWidgets.QTreeWidgetItem(nodoNegacion)
                self.expresionLogica1.construirArbol(ramaNegacion)
                
                if self.expresionAuxiliarLogica != None:
                    nodoOperadorAux = QtWidgets.QTreeWidgetItem(arbol)
                    self.expresionAuxiliarLogica.construirArbol(nodoOperadorAux)
                    ramaLogica2 = QtWidgets.QTreeWidgetItem(nodoOperadorAux)
                    self.expresionLogica2.construirArbol(ramaLogica2) 
                else:
                    ramaLogica2 = QtWidgets.QTreeWidgetItem(arbol)
                    self.expresionLogica2.construirArbol(ramaLogica2)     
                
            
            elif self.operador1 != None and self.operador1.categoria == Categoria.OperadorLogico:
                nodoOperador1 = QtWidgets.QTreeWidgetItem(arbol)
                nodoOperador1.setText(0, self.operador1.lexema)
                ramaLogica1 = QtWidgets.QTreeWidgetItem(nodoOperador1)
                ramaLogica2 = QtWidgets.QTreeWidgetItem(nodoOperador1)
                
                self.expresionLogica1.construirArbol(ramaLogica1)
                self.expresionLogica2.construirArbol(ramaLogica2)
               
                
                if self.expresionAuxiliarLogica != None:
                    nodoOperadorAux = QtWidgets.QTreeWidgetItem(arbol)
                    self.expresionAuxiliarLogica.construirArbol(nodoOperadorAux)
                    ramaLogica3 = QtWidgets.QTreeWidgetItem(nodoOperadorAux)
                    self.expresionLogica3.construirArbol(ramaLogica3) 
                else:
                    ramaLogica3 = QtWidgets.QTreeWidgetItem(arbol)
                    self.expresionLogica3.construirArbol(ramaLogica3)
                
        else:
            
            if self.operador1 != None and self.operador1.lexema == "!":
                
                arbol.setText(0, self.operador1.lexema)
                ramaNegacion = QtWidgets.QTreeWidgetItem(arbol)
                self.expresionLogica1.construirArbol(ramaNegacion)
                

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
                
                
                
                   
                
                
                
                   

        