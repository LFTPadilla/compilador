from logica.sintactico.Sentencia import Sentence

class Imprimir(Sentence):

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

    def getArbolVisual(self):
        return None