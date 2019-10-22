"""
    <Arreglo>::= array <tipoDato> identificador "=" "[" <listaExpresiones> "]" ";"
"""
class Array:

    def __init__(self, tipoDato, identificador, listaExpresiones):
        self.tipoDato = tipoDato
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def __repr__(self):
        return "(Arreglo: tipoDato: %s, identificador: %s, listaExpresiones: %s)" % (self.tipoDato, self.identificador, self.listaExpresiones)

    def __str__(self):
        return "Arreglo [ %s, %s, %s]"% (self.tipoDato, self.identificador, self.listaExpresiones)
    
    def construirArbol(self, arbol, n):
        pass