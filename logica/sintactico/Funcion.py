from PyQt5 import QtWidgets

"""
    <Funcion> ::= [<visibilidad>] <TipoRetorno> Identificador "(" [<ListaParamentros>] ")" "{" <bloqueSentencias> "}"
"""
class Function:

    def __init__(self, visibilidad, retorno, identificador, parametros, bloque):
        self.visibilidad = visibilidad
        self.identificador = identificador
        self.parametros = parametros
        self.retorno = retorno
        self.bloque = bloque


    def getTiposParametros():
        l = []
        for p in self.parametros:
            l.add(p.tipoDato.lexema) #p.getTipoDatos().getLexema()
    

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos):
        tablaSimbolos.guardarSimboloFuncion(self.nombre.lexema,self.retorno.lexema,self.parametros)
        bloque.llenarTablaSimbolos(tablaSimbolos,erroresSemanticos,self.identificador)


    def construirArbol(self, arbol, n):
        arbolFuncion = QtWidgets.QTreeWidgetItem(arbol)

        titulo = "Funcion "+str(n)
        arbolFuncion.setText(0,titulo)

        if self.visibilidad != None:
            ramaVisibilidad = QtWidgets.QTreeWidgetItem(arbolFuncion)
            ramaVisibilidad.setText(0,"Visibilidad "+self.visibilidad.lexema)
          
        ramaRetorno = QtWidgets.QTreeWidgetItem(arbolFuncion)
        ramaRetorno.setText(0,"Retorno "+self.retorno.lexema)
        
        ramaIdentificador = QtWidgets.QTreeWidgetItem(arbolFuncion)
        ramaIdentificador.setText(0,"Identificador "+self.identificador.lexema)

        if len(self.parametros) > 0:
            ramaParametro = QtWidgets.QTreeWidgetItem(arbolFuncion)
            ramaParametro.setText(0,"Parametros")
            cont = 0

            for parametro in self.parametros:
                parametro.construirArbol(ramaParametro, cont)
                cont += 1

        self.bloque.construirArbol(arbolFuncion)

    def __repr__(self):
        return "(Funcion: visibilidad: %s, identificador: %s, parametros: %s, retorno: %s, bloqueSentencias: %s)" % (self.visibilidad, self.identificador, self.parametros, self.retorno, self.bloque)

    def __str__(self):
        return "Funcion [%s, %s, %s, %s, %s]"% (self.visibilidad, self.identificador, self.parametros, self.retorno, self.bloque)

