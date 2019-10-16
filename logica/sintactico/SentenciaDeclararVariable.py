from Sentencia import Sentence

class DeclaracionVariable(Sentence):

    def __init__(self,tipoRetorno, identificador, expresion):
        self.tipoRetorno = tipoRetorno
        self.identificador = identificador
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Declaracion Variable: tipoRetorno: %s, identificador: %s, expresion: %s)" % (self.tipoRetorno, self.identificador, self.expresion)

    def __str__(self):
        return "Sentencia Declaracion Variable [%s, %s, %s]"% (self.tipoRetorno, self.identificador, self.expresion)
    
    def getArbolVisual(self):