from logica.sintactico.Sentencia import Sentence

class Decision(Sentence):

    def __init__(self,sentencia_if, sentencia_else):
        self.sentencia_if = sentencia_if
        self.sentencia_else = sentencia_else


    def __repr__(self):
        return "(Sentencia If Else: SentenciasIF: %s, SentenciasELSE: %s)" % (self.sentencia_if, self.sentencia_else)

    def __str__(self):
        return "Sentencia Decision [%s, %s]"% (self.sentencia_if, self.sentencia_else)
                
    def getArbolVisual(self):
        return None