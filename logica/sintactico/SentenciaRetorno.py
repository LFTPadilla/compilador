from logica.sintactico.Sentencia import Sentence

class Retorno(Sentence):

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Retorno: expresion: %s)" % (self.expresion)

    def __str__(self):
        return "Sentencia Retorno [%s]"% (self.expresion)