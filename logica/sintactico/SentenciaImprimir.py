from Sentencia import Sent

class Imprimir(Sent):

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Imprimir: expresion: %s)" % (self.expresion)

    def __str__(self):
        return "Sentencia Imprimir [%s]"% (self.expresion)

    def __init__(self, identificador):
        self.identificador = identificador

    def __repr__(self):
        return "(Sentencia Imprimir: identificador: %s)" % (self.identificador)

    def __str__(self):
        return "Sentencia Imprimir [%s]"% (self.identificador)