class IfElse:

    def __init__(self,expLogica,bloque_sentencia_if, bloque_sentencia_else):
        self.expLogica = expLogica
        self.bloque_sentencia_if = bloque_sentencia_if
        self.bloque_sentencia_else = bloque_sentencia_else
        
    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.expLogica, self.bloque_sentencia_if,self.bloque_sentencia_else)

    def __str__(self):
        return "Funcion [ %s, %s, %s]"% (self.expLogica, self.bloque_sentencia_if,self.bloque_sentencia_else)