class UnidadComp:

    def __init__(self, listaFunciones):
        self.listaFunciones = listaFunciones
    
    def llenarTablaSimbolos(self, tablaSimbolos, erroresSemanticos):
        for fun in self.listaFunciones:
            fun.llenarTablaSimbolos(tablaSimbolos,erroresSemanticos)

    def analisisSemantico(self,tablaSimbolos,listaErrores):
        for fun in self.listaFunciones:
            fun.analisisSemantico(tablaSimbolos,listaErrores)

    def obtenerPythonCode(self):
        codigo = "#include <map> \n #include <iostream> "
        for fun in self.listaFunciones:
            codigo += fun.obtenerPythonCode()
            codigo += "\n"
        return codigo