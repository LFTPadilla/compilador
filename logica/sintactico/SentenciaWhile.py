class While(Sentencia):

    def __init__(self, expresionLogica, bloque_sentencias):
        self.expresionLogica = expresionLogica
        self.bloque_sentencias = bloque_sentencias

    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.expresionLogica, self.bloque_sentencias)

    def __str__(self):
        return "Funcion [ %s, %s]"% (self.expresionLogica, self.bloque_sentencias)