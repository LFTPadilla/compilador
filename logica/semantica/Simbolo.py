class Symbol:
    
    def __init__(self, nombre, tipoDato, fila, columna, ambito, expresion, tipoRetorno, tipoParametros):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.ambito = ambito
        self.expresion = expresion
        self.tipoRetorno = tipoRetorno
        self.tipoParametros = tipoParametros
        self.fila = fila
        self.columna = columna
        
    def __str__(self):
        return "SIMBOLO[nombre: %s|TipoVariable: %s|Ambito: %s|Expresion: %s|TipoParametros: %s| TipoRetorno: %s]"%(self.nombre,self.tipoDato,self.ambito,self.expresion,self.tipoParametros, self.tipoRetorno)
        