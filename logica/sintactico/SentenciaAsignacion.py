class Asignacion(Sentencia):

    def __init__(self, identificador, operadorAsignacion, expresion):
        self.identificador = identificador
        self.operadorAsignacion = operadorAsignacion
        self.expresion = expresion

    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.identificador, self.operadorAsignacion, self.expresion)

    def __str__(self):
        return "Funcion [ %s, %s, %s]"% (self.identificador, self.operadorAsignacion, self.expresion)