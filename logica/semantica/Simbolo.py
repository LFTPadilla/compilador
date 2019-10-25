class simbolito:
    nombre = None
    tipoDato = None
    ambito = None
    expresion = None
    tipoRetorno = None
    tipoParametros = []
    
    def _init_(self, nombre, tipoDato, ambito, expresion, tipoRetorno, tipoParametros):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.ambito = ambito
        self.expresion = expresion
        self.tipoRetorno = tipoRetorno
        self.tipoParametros = tipoParametro