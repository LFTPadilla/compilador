
from Token import Token
from Categoria import Categoria

class Analizador:
    private__ = ""
    codigo = ""
    tokens = []
    caracterActual = ""
    finCodigo = "¿"
    posicionActual = 0
    filaActual = 0
    colActual = 0

    def __init__(self,codigo):
        self.codigo = codigo
        self.caracterActual = self.codigo[self.posicionActual]



    def analizar(self):
        while(self.caracterActual != self.finCodigo):   
            
            if(self.caracterActual=="\n" or self.caracterActual=="\t" or self.caracterActual == " "):
                self.obtenerSiguienteCaracter()
                continue

            if (self.esNatural()) :
                continue
            
            if (self.esOperadorLogico()):
                continue
        
            self.tokens.append(Token(self.caracterActual, Categoria.Desconocido, self.filaActual, self.colActual)) 
            self.obtenerSiguienteCaracter()

    def esOperadorLogico(self):
        print(self.caracterActual,"Entroooo")
        if(self.caracterActual == "&"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual== "&"):
                self.tokens.append(Token("&&", Categoria.OperadorLogico,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False

        if(self.caracterActual == "|"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual== "|"):
                self.tokens.append(Token("||", Categoria.OperadorLogico,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
        
        if(self.caracterActual == "!"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual== "="):
                self.tokens.append(Token("!=", Categoria.OperadorLogico,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
        
        if(self.caracterActual == "="):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            print(self.caracterActual,"eeee")
            if(self.caracterActual== "="):
                self.tokens.append(Token("==", Categoria.OperadorLogico,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False    



    def esNatural(self):
              
        if(self.caracterActual.isdigit()):  
            lexema = ""          
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            
            lexema += self.caracterActual 
            
            self.obtenerSiguienteCaracter()
            while(self.caracterActual.isdigit()):
                lexema += self.caracterActual
                self.obtenerSiguienteCaracter()
            
            if(self.caracterActual == '.'):
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
            else:
                self.tokens.append(Token(lexema, Categoria.NumeroNatural,self.filaActual,self.colActual)) 
                return True                                 
        else:
            return False        
        

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

    def hacerBT(self, posInicial, filaInicial, columnaInicial):
        self.posicionActual = posInicial
        self.filaActual = filaInicial
        self.colActual = columnaInicial
        self.caracterActual = self.codigo[self.posicionActual]
    

