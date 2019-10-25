from logica.semantica.Simbolo import simbolito

class tabla:
    #crear simbolo
    #buscar simbolo

    listaSimbolos = None
    def _init_ (self):
        listaSimbolos = []

    def buscarSimboloVariable(self, nombre, ambito):
        for simbolo in self.listaSimbolos:
            if simbolo.ambito != None:
                if simbolo.nombre == nombre and simbolo.ambito == ambito:
                    return simbolo

    def guardarSimboloVariable(self, nombre, tipoDato, ambito, expresion):
        sim = self.buscarSimboloVariable (nombre, ambito)

        if sim == None:
            s = simbolito (nombre, tipoDato, ambito, expresion, None, None)
            listaSimbolos.append(s)
        else:
            #reportar error
            pass

    def buscarSimboloFuncion(self, nombre, tipoRetorno):
        for simbolo in self.listaSimbolos:
            if simbolo.tipoRetorno != None:
                if simbolo.nombre == nombre and simbolo.tipoRetorno == tipoRetorno:
                    return simbolo

    def guardarSimboloFuncion(self, nombre, tipoRetorno, tipoParametros):
        sim = self.buscarSimboloFuncion (nombre, tipoRetorno)
        if sim == None:
            s = simbolito (nombre, None, None, None, tipoRetorno, tipoParametros)
            listaSimbolos.append(s)
        else:
            pass
            #reportar error