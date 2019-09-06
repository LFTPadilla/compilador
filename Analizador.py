
class AnalizadorLexico():
    codigo = ""
    tokens = []
    caracterActual = ''
    finCodigo = "¿"
    posicionActual = 0
    filaActual = 0
    colActual = 0

    def __init__(self,codigo):
        self.codigo = codigo



    def analizar(self):
        while(self.caracterActual != self.finCodigo):
            
            if(self.caracterActual==" "):
                self.obtenerSiguienteCaracter()
                continue    
            
            if(self.caracterActual=="\n" or self.caracterActual=="\t"):
                self.obtenerSiguienteCaracter()
                continue

            if(self.esReal()):
                continue

            if(self.esEntero()):
               continue
            
            if(self.esReal()):
                continue

            if(self.esIncrementoDecremento(6)):
                continue

    

    def esIncrementoDecremento(self, y):
        return False
    
    def esIncremento(self,x):
        return True
            
    def esEntero(self):
        return False
    
    def esReal(self):
        return True

    def obtenerSiguienteCaracter(self):
        self.posicionActual+=1
        if(self.posicionActual < len(self.codigo) ):
            if(self.caracterActual == "\n"):
                self.filaActual+=1
                self.colActual = 0
            else:
                self.colActual+=1
            self.caracterActual = self.codigo[self.posicionActual]
        else:
            self.caracterActual = self.finCodigo

    

