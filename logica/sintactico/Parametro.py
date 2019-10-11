class Parametro:
    def __init__(self,tipoRetorno, identificador):
        self.tipoRetorno = tipoRetorno
        self.identificador = identificador

    def __repr__(self):
        return "(Parametro: tipoRetorno: %s, identificador: %s)" % (self.tipoRetorno, self.identificador)

    def __str__(self):
        return "Parametro [%s, %s]" % (self.tipoRetorno, self.identificador)