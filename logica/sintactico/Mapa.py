class mapita:

    def __init__(self, identificador, listaComponentes):
        self.identificador = identificador
        self.listaComponentes = listaComponentes

    def __repr__(self):
        return "(Mapa: identificador: %s listaComponentes: %s)" % (self.identificador, self.listaComponentes)

    def __str__(self):
        return "Mapa [%s, %s]" % (self.identificador, self.listaComponentes)