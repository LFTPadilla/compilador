class SentIF:

    def __init__(self, expresionLogica, bloqueSentencias):
        self.expresionLogica = expresionLogica
        self.bloqueSentencias = bloqueSentencias


    def __repr__(self):
        return "(Sentencia If : ExpresionLogica: %s, bloqueSentencias: %s)" % (self.expresionLogica, self.bloqueSentencias)

    def __str__(self):
        return "Sentencia If [%s, %s]"% (self.expresionLogica, self.bloqueSentencias)
                
    def getArbolVisual(self):
        return None