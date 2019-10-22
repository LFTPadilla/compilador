class SentELSE:

    def __init__(self, bloqueSentencias):
        self.bloqueSentencias = bloqueSentencias

    def __repr__(self):
        return "(Sentencia Else : bloqueSentencias: %s)" % (self.bloqueSentencias)

    def __str__(self):
        return "Sentencia Else [%s]"% (self.bloqueSentencias)
                
    def getArbolVisual(self):
        return None