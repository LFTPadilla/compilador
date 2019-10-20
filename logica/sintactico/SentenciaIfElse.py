from compilador.logica.sintactico.Sentencia import Sentence

class IfElse(Sentence):

    def __init__(self,expresionLogica,bloque_sentencia_if, bloque_sentencia_else):
        self.expresionLogica = expresionLogica
        self.bloque_sentencia_if = bloque_sentencia_if
        self.bloque_sentencia_else = bloque_sentencia_else


    def __repr__(self):
        return "(Sentencia If Else: expresionLogica: %s, bloqueSentenciasIF: %s, bloqueSentenciasELSE: %s)" % (self.expresionLogica, self.bloque_sentencia_if, self.bloque_sentencia_else)

    def __str__(self):
        return "Sentencia If Else [%s, %s, %s]"% (self.expresionLogica, self.bloque_sentencia_if, self.bloque_sentencia_else)
                
    def getArbolVisual(self):
        return None