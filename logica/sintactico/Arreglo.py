class Array:

    def __init__(self, tipoRetorno, identificador, listaExpresiones):
        self.tipoRetorno = tipoRetorno
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def __repr__(self):
        return "(Arreglo: tipoRetorno: %s, identificador: %s, listaExpresiones: %s)" % (self.tipoRetorno, self.identificador, self.listaExpresiones)

    def __str__(self):
        return "Arreglo [ %s, %s, %s]"% (self.tipoRetorno, self.identificador, self.listaExpresiones)