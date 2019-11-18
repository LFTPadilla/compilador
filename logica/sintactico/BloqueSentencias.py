from PyQt5 import QtWidgets
"""
        <BloqueSentencia> ::= "{" [<listaSentencias>] "}"
"""
class bloqueSent:
    
    def __init__(self, listaSentencias):
        self.listaSentencias = listaSentencias

    def __repr__(self):
        return "(BloqueSentencias: listaSentencias: %s)" % (self.listaSentencias)

    def __str__(self):
        return "BloqueSentencias [%s]" % ( self.listaSentencias)

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos,ambito):
        print("ahora las sentencias")
        
        for sentencia in self.listaSentencias:
            print("Voy a meter ",sentencia)
            
            sentencia.llenarTablaSimbolos(tablaSimbolos,erroresSemanticos,ambito)

    def analisisSemantico(self,tablaSimbolos,listaErrores, ambito):
        for sentencia in self.listaSentencias:
            #A la ultima sentencia (return) se le manda el ambito(el nombre de la funcion que la contiene)
            if sentencia == self.listaSentencias[-1]:
                sentencia.analisisSemantico(tablaSimbolos,listaErrores, ambito)
            else:    
                sentencia.analisisSemantico(tablaSimbolos,listaErrores)


    def obtenerPythonCode(self):
        codigo = ""
        for sentencia in self.listaSentencias:
            codigo += sentencia.obtenerPythonCode()
            codigo += "\n"
        return codigo

    def construirArbol(self, arbol):
        arbolBloque = QtWidgets.QTreeWidgetItem(arbol)
        arbolBloque.setText(0,"Bloque Sentencias")

        if len(self.listaSentencias) > 0:
            ramaListaSent = QtWidgets.QTreeWidgetItem(arbolBloque)
            ramaListaSent.setText(0,"listaSentencias")

            
            for sentencia in self.listaSentencias:
                sentencia.construirArbol(ramaListaSent)
