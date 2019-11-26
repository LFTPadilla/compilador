from PyQt5 import QtWidgets
from logica.sintactico.Sentencia import Sentence
"""
    <InvocarMetodo>::= invocar identificador "("[<ListaArgumentos>]")" ";"
"""
class InvocarFuncion(Sentence):

    def __init__(self, identificador, listaArgumentos):
        self.identificador = identificador
        self.listaArgumentos = listaArgumentos

    def __repr__(self):
        return "(Sentencia Invocar Funcion: identificador: %s, listaArgumentos: %s)" % (self.identificador, self.listaArgumentos)

    def __str__(self):
        return "Sentencia Invocar Funcion [%s, %s]"% (self.identificador, self.listaArgumentos)
    
    def analisisSemantico(self,tablaSimbolos,listaErrores):
        for simbolo in tablaSimbolos.listaSimbolos:
            if simbolo.nombre == self.identificador.lexema and simbolo.tipoRetorno!=None:
                return True
        err = "La funcion \""+self.identificador.lexema+"\" no se encuentra declarada."
        print("err "+err)
        listaErrores.append(err)

    def obtenerPythonCode(self):
        codigo = ""
        codigo = self.identificador.obtenerPythonCode() + "("
        if len(self.listaArgumentos) > 0:
            for argumento in self.listaArgumentos:
                codigo += argumento.obtenerPythonCode()
                codigo += ", "
            codigo =  codigo[:-2]
        codigo += ");"
        return codigo

    def construirArbol(self, arbol):
        arbolInvocarFuncion = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "InvocarFuncion "
        arbolInvocarFuncion.setText(0,titulo)

        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolInvocarFuncion)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

        
        if len(self.listaArgumentos) > 0:
            ramaListaArgumentos = QtWidgets.QTreeWidgetItem(arbolInvocarFuncion)
            ramaListaArgumentos.setText(0,"Argumentos ")
            cont = 0
            
            for argumento in self.listaArgumentos:
                argumento.construirArbol(ramaListaArgumentos, cont)
                cont += 1

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos, ambito):
        pass

    
    
