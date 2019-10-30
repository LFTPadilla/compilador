class UnidadComp:

    def __init__(self, listaFunciones):
        self.listaFunciones = listaFunciones
    
    def llenarTablaSimbolos(tablaSimbolos, erroresSemanticos):
        for fun in self.listaFunciones:
            fun.llenarTablaSimbolos(tablaSimbolos,erroresSemanticos)
    