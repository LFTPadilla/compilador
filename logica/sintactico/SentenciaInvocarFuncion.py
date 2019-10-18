from logica.sintactico.Sentencia import Sentence

class InvocarFuncion(Sentence):

    def __init__(self, identificador, listaArgumentos):
        self.identificador = identificador
        self.listaArgumentos = listaArgumentos

    def __repr__(self):
        return "(Sentencia Invocar Funcion: identificador: %s, listaArgumentos: %s)" % (self.identificador, self.listaArgumentos)

    def __str__(self):
        return "Sentencia Invocar Funcion [%s, %s]"% (self.identificador, self.listaArgumentos)