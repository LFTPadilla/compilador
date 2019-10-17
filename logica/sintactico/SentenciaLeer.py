from Sentencia import Sentence

class Leer(Sentence):

    def __init__(self, expresion):
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Leer: expresion: %s)" % (self.expresion)

    def __str__(self):
        return "Sentencia Leer [%s]"% (self.expresion)
    
    def getArbolVisual(self):
        
