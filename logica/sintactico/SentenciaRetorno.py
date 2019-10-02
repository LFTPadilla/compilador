class Retorno:

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.expresion)

    def __str__(self):
        return "Funcion [ %s]"% (self.expresion)