class Fun:

    def __init__(self,nombre,parametros, retorno, bloque):
        self.nombre = nombre
        self.parametros = parametros
        self.retorno = retorno
        self.bloque = bloque

    def __repr__(self):
        return "(Funcion: %s, %s,Fila: %s,Columna: %s)" % (self.nombre, self.parametros,self.retorno,self.bloque)

    def __str__(self):
        return "Funcion [ %s, %s, %s, %s]"% (self.nombre, self.parametros,self.retorno,self.bloque)