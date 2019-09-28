from logica.lexico.Categoria import Categoria

class Token:
    
    lexema = ""
    fila = -1
    columna = -1
    categoria = Categoria.Desconocido
    
    
    def __init__(self, lexema,categoria,fila,columna):
        self.lexema = lexema
        self.categoria = categoria
        self.fila = fila
        self.columna = columna
    def __repr__(self):
        return "(Lexema: %s, %s,Fila: %s,Columna: %s)" % (self.lexema, self.categoria,self.fila,self.columna)

    def __str__(self):
        return "[ %s, %s, %s, %s]"% (self.lexema, self.categoria,self.fila,self.columna)

    
    
        
