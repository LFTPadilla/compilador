from logica.lexico.Categorias import Categoria

class Token:
    
    lexema = ""
    fila = -1
    _columna = -1
    categoria = Categoria.Desconocido
    
    
    def __init__(self, lexema,categoria,fila,columna):
        self.lexema = lexema
        self.categoria = categoria
        self.fila = fila
        self.columna = columna
    
    def obtenerPythonCode(self):
        if self.categoria == Categoria.PalabraReservada:
            
            if self.lexema == "boolean":
                return "bool"
            
            if self.lexema == "String":
                return "char[]"

            
    
    def __repr__(self):
        return "(Lexema: %s, %s,Fila: %s,Columna: %s)" % (self.lexema, self.categoria,self.fila,self.columna)

    def __str__(self):
        return "[ %s, %s, %s, %s]"% (self.lexema, self.categoria,self.fila,self.columna)

    
    
        
