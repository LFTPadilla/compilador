from PyQt5 import QtWidgets
from logica.sintactico.SentenciaRetorno import Retorno

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
        retorno = False
        for sentencia in self.listaSentencias:
            #A la ultima sentencia (return) se le manda el ambito(el nombre de la funcion que la contiene)
            if isinstance(sentencia,Retorno):
                retorno = True
                sentencia.analisisSemantico(tablaSimbolos,listaErrores, ambito)
            else:    
                sentencia.analisisSemantico(tablaSimbolos,listaErrores)
        
        funcion = None        
        for simbolo in tablaSimbolos.listaSimbolos:
            if simbolo.tipoRetorno != None:                
                if simbolo.nombre == ambito:                    
                    funcion = simbolo
                    break
                    
                
        if retorno == False and funcion.tipoRetorno != "void":
            listaErrores.append("La funcion requiere de un retorno")
            
        

    def obtenerPythonCode(self):
        codigo = "{"
        for sentencia in self.listaSentencias:
            codigo += sentencia.obtenerPythonCode()
            codigo += "\n"
        codigo += "}"
        return codigo

    def construirArbol(self, arbol):
        arbolBloque = QtWidgets.QTreeWidgetItem(arbol)
        arbolBloque.setText(0,"Bloque Sentencias")

        if len(self.listaSentencias) > 0:
            ramaListaSent = QtWidgets.QTreeWidgetItem(arbolBloque)
            ramaListaSent.setText(0,"listaSentencias")

            
            for sentencia in self.listaSentencias:
                sentencia.construirArbol(ramaListaSent)
