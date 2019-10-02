class Parameto:
    def __init__(self,tipo_dato,nombre):
        self.tipo_dato = tipo_dato
        self.nombre = nombre

    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.tipo_dato, self.nombre)

    def __str__(self):
        return "Funcion [ %s, %s]"% (self.tipo_dato, self.nombre)