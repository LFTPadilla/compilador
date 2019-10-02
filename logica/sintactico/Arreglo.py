class Arreglo:

    def __init__(self, tipoRetorno, identificador, listaExpresiones):
        self.tipoRetorno = tipoRetorno
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.tipoRetorno, self.identificador, self.listaExpresiones)

    def __str__(self):
        return "Funcion [ %s, %s, %s]"% (self.tipoRetorno, self.identificador, self.listaExpresiones)