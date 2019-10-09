class InvocarFuncion:

    def __init__(self, nombre, listaArgumentos):
        self.nombre = nombre
        self.listaArgumentos = listaArgumentos

    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.nombre, self.listaArgumentos)

    def __str__(self):
        return "Funcion [%s, %s]"% (self.nombre, self.listaArgumentos)