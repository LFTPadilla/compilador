class Argument:

    def __init__(self, identificador):
        self.identificador = identificador

    def __repr__(self):
        return "(Argumento:  identificador: %s)" % (self.identificador)

    def __str__(self):
        return "Argumento [ %s]"% (self.identificador)
