class DeclaracionVariable:

    def __init__(self,retorno, nombre, expresion):
        self.retorno = retorno
        self.nombre = nombre
        self.expresion = expresion
        self.bloque = bloque

    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.retorno, self.nombre,self.expresion)

    def __str__(self):
        return "Funcion [ %s, %s, %s]"% (self.retorno, self.nombre,self.expresion)