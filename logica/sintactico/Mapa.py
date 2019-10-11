class map:

    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor

    def __repr__(self):
        return "(Parametro: tipoRetorno: %s, identificador: %s)" % (self.llave, self.valor)

    def __str__(self):
        return "Parametro [%s, %s]" % (self.llave, self.valor)