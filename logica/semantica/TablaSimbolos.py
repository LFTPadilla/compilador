from logica.semantica.Simbolo import Symbol

class SymbolTable:
    #crear simbolo
    #buscar simbolo

    
    def _init_ (self):
        self.listaSimbolos = []
        self.listaErrores = []


    """
	    Permite guardar un símbolo de tipo variable en la tabla de símbolos 
	"""
    def guardarSimboloVariable(self, nombre, tipoDato,fila, columna, ambito, expresion):
        sim = self.buscarSimboloVariable (nombre, ambito,fila, columna)

        if sim == None:
            s = Symbol(nombre, tipoDato, fila,columna, ambito, expresion, None, None)
            self.listaSimbolos.append(s)
            return s
        else:
            self.listaErrores.append("La variable "+nombre+" ya existe")
        return None

    """
	 * Permite guardar un símbolo de tipo función en la tabla de símbolos 
	"""
    def guardarSimboloFuncion(self, nombre, tipoRetorno, tipoParametros):
        sim = self.buscarSimboloFuncion (nombre, tipoParametros)
        if sim == None:
            s = Symbol (nombre, None, None, None, tipoRetorno, tipoParametros)
            listaSimbolos.append(s)
            return s
        else:
            self.listaErrores.append("La funcion "+nombre+" ya existe")
        
        return None

    def buscarSimboloVariable(self, nombre, ambito,fila,columna):
        for simbolo in self.listaSimbolos:
            if simbolo.ambito != None:
                if simbolo.nombre == nombre and simbolo.ambito == ambito:
                    return simbolo
        return None


    def buscarSimboloFuncion(self, nombre, tipoParametros):
        for simbolo in self.listaSimbolos:
            #Al verificar que el tipo de retorno sea diferente de None se verifica que es una funcion
            if simbolo.tipoRetorno != None:
                #preguntar por que compara un arraylist tipoParametros
                if simbolo.nombre == nombre and simbolo.parametros() == tipoParametros:
                    return simbolo
        return None
    