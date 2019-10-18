class mapita:

    def __init__(self, listaComponentes):
        self.listaComponentes = listaComponentes

    def __repr__(self):
        return "(Mapa: listaComponentes: %s)" % (self.listaComponentes)

    def __str__(self):
        return "Mapa [%s]" % (self.listaComponentes)