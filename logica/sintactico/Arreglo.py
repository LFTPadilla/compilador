"""
    <Arreglo>::= array <tipoDato> identificador "=" "[" <listaExpresiones> "]" ";"
"""
from PyQt5 import QtWidgets
class Array:

    def __init__(self, tipoDato, identificador, listaExpresiones):
        self.tipoDato = tipoDato
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def __repr__(self):
        return "(Arreglo: tipoDato: %s, identificador: %s, listaExpresiones: %s)" % (self.tipoDato, self.identificador, self.listaExpresiones)

    def __str__(self):
        return "Arreglo [ %s, %s, %s]"% (self.tipoDato, self.identificador, self.listaExpresiones)
    
    def construirArbol(self, arbol):

        arbolArreglo = QtWidgets.QTreeWidgetItem(arbol)
        arbolArreglo.setText(0,"Arreglo ")

        ramaTipoDato = QtWidgets.QTreeWidgetItem(arbolArreglo)
        ramaTipoDato.setText(0,"Tipo Dato "+self.tipoDato.lexema)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolArreglo)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)
        
        if len(self.listaExpresiones) >0:
            ramaElementos = QtWidgets.QTreeWidgetItem(arbolArreglo)
            ramaElementos.setText(0,"ListaExpresiones ")
            
            for exp in self.listaExpresiones:
                arbolExpresion = QtWidgets.QTreeWidgetItem(ramaElementos)
                exp.construirArbol(arbolExpresion)

    def obtenerPythonCode(self):
        codigo = ""
        codigo += self.tipoDato.obtenerPythonCode() + " "
        codigo += self.identificador.obtenerPythonCode() + "["+ len(self.listaExpresiones) +"]"
        codigo += " = "
        codigo += "{"
        for expresion in self.listaExpresiones:
            codigo += expresion.obtenerPythonCode()
            codigo += ","
        codigo = codigo[:-1]
        codigo +="} ;"
        return codigo

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass
    