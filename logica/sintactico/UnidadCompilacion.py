class UnidadComp:

    def __init__(self, listaFunciones):
        self.listaFunciones = listaFunciones
    
    def llenarTablaSimbolos(self, tablaSimbolos, erroresSemanticos, ambito):
        for fun in self.listaFunciones:
            fun.llenarTablaSimbolos(tablaSimbolos,erroresSemanticos)

    