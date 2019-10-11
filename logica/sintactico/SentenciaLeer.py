from Sentencia import Sent

class Leer(Sent):

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Leer: expresion: %s)" % (self.expresion)

    def __str__(self):
        return "Sentencia Leer [%s]"% (self.expresion)
