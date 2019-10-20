from logica.sintactico.Sentencia import Sentence

class Imprimir(Sentence):

    def __init__(self, identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Imprimir: identificador:%s, expresion: %s)" % (self.identificador, self.expresion)

    def __str__(self):
        return "Sentencia Imprimir [%s, %s]"% (self.identificador, self.expresion)

    