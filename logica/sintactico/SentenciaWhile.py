from Sentencia import Sentence

class SentenceWhile(Sentence):

    def __init__(self, expresionLogica, bloque_sentencias):
        self.expresionLogica = expresionLogica
        self.bloque_sentencias = bloque_sentencias

    def __repr__(self):
        return "(Sentencia While: expresionLogica: %s, bloqueSetnecias: %s)" % (self.expresionLogica, self.bloque_sentencias)

    def __str__(self):
        return "Sentencia While [%s, %s]"% (self.expresionLogica, self.bloque_sentencias)
    
    def getArbolVisual(self):
        
