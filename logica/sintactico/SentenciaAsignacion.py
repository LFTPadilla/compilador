from logica.sintactico.Sentencia import Sentence

class Asignacion(Sentence):

    def __init__(self, identificador, operadorAsignacion, expresion):
        self.identificador = identificador
        self.operadorAsignacion = operadorAsignacion
        self.expresion = expresion

    def __repr__(self):
        return "(Sentencia Asignacion: identificador: %s,operadorAsignacion: %s, expresion: %s)" % (self.identificador, self.operadorAsignacion, self.expresion)

    def __str__(self):
        return "Sentencia Asignacion [%s, %s, %s]"% (self.identificador, self.operadorAsignacion, self.expresion)
    
    def getArbolVisual(self):
        return None