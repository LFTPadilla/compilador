class Argument:

    def __init__(self, identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion

    def __repr__(self):
        return "(Argumento:  identificador: %s  expresion: %s)" % (self.identificador, self.expresion)

    def __str__(self):
        return "Argumento [ %s, %s]"% (self.identificador, self.expresion)
