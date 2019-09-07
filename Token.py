from Categoria import Categoria

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
    
    def __str__(self):
        return "(",self.lexema,",",self.categoria,", F:",self.fila,"C:",self.columna,")"
        
    
    
    
        
