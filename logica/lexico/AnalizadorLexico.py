
from logica.lexico.Tokens import Token
from logica.lexico.Categorias import Categoria
import time

class ALexico:
    
    def __init__(self,codigo):
        self.codigo = codigo
        self.caracterActual = self.codigo[0]
        self.palabrasReservadas = [ "String", "abstract", "continue", "for", "new", "switch", "assert", "default", "goto", "package", "synchronized", "boolean", "do", "if", "private", "this", "break", "double", "implements", "protected", "throw", "byte", "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", "catch", "extends", "int", "short", "try", "char", "final", "interface", "static", "void", "class", "finally", "long", "strictfp", "volatile", "const", "float", "native", "super", "while", "map", "array", "invocar", "imprimir", "leer", "let", "asig"]
        self.private__ = ""
        self.tokens = []
        self.finCodigo = "¿"
        self.posicionActual = 0
        self.filaActual = 0
        self.colActual = 0
        self.palabrasReservadas=[]
        self.listaErrores = []
        

    def getListaTokens(self):
        return self.tokens

    def analizar(self):
        while(self.caracterActual != self.finCodigo):   
            
            if(self.caracterActual=="\n" or self.caracterActual=="\t" or self.caracterActual == " "):
                self.obtenerSiguienteCaracter()
                continue
            
            if(self.esParentesis()):
                continue
            
            if(self.esLlaves()):
                continue
            
            if(self.esCorchetes()):
                continue

            if (self.esNatural()) :
                continue

            if (self.esOperadorAritmetico()) :
                continue
            
            if(self.esOperadorRelacional()):
               continue
            
            
            if(self.esCadenaCaracteres()):
                continue
    
            if (self.esNatural()) :
                continue
            
            if (self.esReal()):
                continue
            
            if (self.esPuntosDosPuntos()):
                continue
            
            if (self.esOperadorLogico()):
                continue

            if(self.esComentarioBloque()):
                continue

            if(self.esIncrementoDecremento()):
                continue

            if(self.esCaracter()):
                continue

            if(self.esSeparador()):
                continue

            if(self.esFinSentencia()):
                continue

            if(self.esComentarioLinea()):
                continue

            if (self.esOperadorAsignacion()) :
                continue

            if (self.esOperadorAritmetico()) :
                continue

            if(self.esIdentificador()):
                continue

            self.listaErrores.append(Token(self.caracterActual, Categoria.Desconocido, self.filaActual, self.colActual)) 
            self.obtenerSiguienteCaracter()

    def esFinSentencia(self):
        if(self.caracterActual == ";"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            self.tokens.append(Token(";", Categoria.FinSentencia,self.filaActual,self.colActual)) 
            return True
            

    def esComentarioLinea(self):
        if(self.caracterActual == "/"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "/"):
                self.obtenerSiguienteCaracter()
                palabra = "//"
                
                while(self.caracterActual != "\n" and self.caracterActual != self.finCodigo):
                    palabra += self.caracterActual
                    self.obtenerSiguienteCaracter()
                    
                self.tokens.append(Token(palabra,Categoria.ComentarioLinea,self.filaActual,self.colActual))
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
        else: 
            return False

    def esParentesis(self):
        
        if self.caracterActual == '(':
            self.tokens.append(Token(self.caracterActual,Categoria.ParentesisIzquierdo,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        elif self.caracterActual == ')':
            self.tokens.append(Token(self.caracterActual,Categoria.ParentesisDerecho,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        else:
            return False
        
        
    def esLlaves(self):
           
        if self.caracterActual == '{' :
            self.tokens.append(Token(self.caracterActual,Categoria.LlaveIzquierda,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        elif  self.caracterActual == '}':
            self.tokens.append(Token(self.caracterActual,Categoria.LlaveDerecha,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        else:
            return False        

 
    def esCorchetes(self):
        if self.caracterActual == '[' :            
            self.tokens.append(Token(self.caracterActual,Categoria.CorcheteIzquierdo,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        elif self.caracterActual == ']':
            self.tokens.append(Token(self.caracterActual,Categoria.CorcheteDerecho,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        else:
            return False           
            

    def esSeparador(self):
        if(self.caracterActual == ","):
            self.tokens.append(Token(",",Categoria.Separador,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        else:
            return False

    def esIdentificador(self):
        if(self.caracterActual=="_" or (ord(self.caracterActual)>64 and ord(self.caracterActual)<91) or (ord(self.caracterActual)>96 and ord(self.caracterActual)<123)):
            
            lexema = ""
            
            lexema += self.caracterActual
            self.obtenerSiguienteCaracter()
            
            while(self.caracterActual.isdigit() or self.caracterActual=="_" or  (ord(self.caracterActual)>64 and ord(self.caracterActual)<91) or (ord(self.caracterActual)>96 and ord(self.caracterActual)<123)):
                lexema += self.caracterActual
                self.obtenerSiguienteCaracter()
            
            #Las palabras reservadas estan en un arreglo global
            if lexema in self.palabrasReservadas:
                self.tokens.append(Token(lexema,Categoria.PalabraReservada,self.filaActual,self.colActual))
            else:
                self.tokens.append(Token(lexema,Categoria.Identificador,self.filaActual,self.colActual))
            return True
        else:
            return False

    def esCadenaCaracteres(self):
        if(self.caracterActual=='"'):
            texto = ""
            
            self.obtenerSiguienteCaracter()

            while(self.caracterActual!="\"" and self.caracterActual!=self.finCodigo):
                #print(self.caracterActual,self.caracterActual!="\"")
                aux = self.caracterActual
                texto+=self.caracterActual
                self.obtenerSiguienteCaracter()
                if(aux=="\\"):
                    if(self.caracterActual=="n" or self.caracterActual=="t" or self.caracterActual=="\""):
                        texto+=self.caracterActual
                    else:
                        self.tokens.append(Token("\\"+self.caracterActual, Categoria.ErrorLexico, self.filaActual, self.colActual ))
                
            if(self.caracterActual==self.finCodigo):
                self.tokens.append(Token(texto, Categoria.ErrorLexico, self.filaActual, self.colActual ))
            else:
                self.obtenerSiguienteCaracter()
                self.tokens.append(Token('"'+texto+'"',Categoria.CadenaCaracteres,self.filaActual,self.colActual))
            return True
        else:
            return False

    def esCaracter(self):
        
        if(self.caracterActual=="'"):
            
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            letra = self.caracterActual
            self.obtenerSiguienteCaracter()
            
            if(self.caracterActual=="'"):
                self.obtenerSiguienteCaracter()
                self.tokens.append(Token("'"+letra+"'",Categoria.Caracter,self.filaActual,self.colActual))
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
        else:
            return False

    def esComentarioBloque(self):
        err = False
        if(self.caracterActual == "/"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "*"):
                self.obtenerSiguienteCaracter()
                lexema = "/*"+self.caracterActual
                bucle = True
                while(bucle):
                    if(self.caracterActual=="*"):
                        self.obtenerSiguienteCaracter()
                        if(self.caracterActual=="/"):
                            lexema += "*/"
                            bucle=False
                        else:
                            lexema += self.caracterActual
                    else:
                        if(self.posicionActual==len(self.codigo)-1):
                            self.tokens.append(Token('"'+lexema+'"',Categoria.ErrorLexico,self.filaActual,self.colActual))
                            self.obtenerSiguienteCaracter()
                            err = True
                            break
                        else:
                            lexema += self.caracterActual
                            self.obtenerSiguienteCaracter()
                if(not(err)):
                    self.tokens.append(Token(lexema, Categoria.ComentarioBloque,self.filaActual,self.colActual)) 
                    self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False

    def esPuntosDosPuntos(self):
        if(self.caracterActual == ":"):
            self.tokens.append(Token(self.caracterActual,Categoria.DosPuntos,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        elif self.caracterActual == ".":
            self.tokens.append(Token(self.caracterActual,Categoria.Punto,self.filaActual,self.colActual))
            self.obtenerSiguienteCaracter()
            return True
        else:
            return False
    
    def esIncrementoDecremento(self):
        if(self.caracterActual == "+"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "+"):
                self.tokens.append(Token("++", Categoria.OperadorIncrementoDecremento,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
                
        if(self.caracterActual == "-"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "-"):
                self.tokens.append(Token("--", Categoria.OperadorIncrementoDecremento,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False

    def esOperadorAritmetico(self):
        if(self.caracterActual == "+"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "+" or self.caracterActual == "="):
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
            else:
                self.tokens.append(Token("+", Categoria.OperadorAritmetico,self.filaActual,self.colActual))                 
                return True
        
        if(self.caracterActual == "-"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "-" or self.caracterActual == "="):
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
            else:
                self.tokens.append(Token("-", Categoria.OperadorAritmetico,self.filaActual,self.colActual)) 
                return True

        if(self.caracterActual == "*"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "*" or self.caracterActual == "=" or self.caracterActual == "/"):
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
            else:
                self.tokens.append(Token("*", Categoria.OperadorAritmetico,self.filaActual,self.colActual)) 
                return True
        
        if(self.caracterActual == "/"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "/" or self.caracterActual == "=" or self.caracterActual == "*"):
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
            else:
                self.tokens.append(Token("/", Categoria.OperadorAritmetico,self.filaActual,self.colActual)) 
                return True
        
        if(self.caracterActual == "%"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "="):
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
            else:
                self.tokens.append(Token("%", Categoria.OperadorAritmetico,self.filaActual,self.colActual)) 
                return True

    def esOperadorAsignacion(self):
        if(self.caracterActual == "+"):
            
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            
            if(self.caracterActual == "="):
                self.tokens.append(Token("+=", Categoria.OperadorAsignacion,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
        
        if(self.caracterActual == "-"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "="):
                self.tokens.append(Token("-=", Categoria.OperadorAsignacion,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False

        if(self.caracterActual == "*"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "="):
                self.tokens.append(Token("*=", Categoria.OperadorAsignacion,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False        

        if(self.caracterActual == "/"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "="):
                self.tokens.append(Token("/=", Categoria.OperadorAsignacion,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False
        
        if(self.caracterActual == "%"):
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posInicial = self.posicionActual
            self.obtenerSiguienteCaracter()
            if(self.caracterActual == "="):
                self.tokens.append(Token("%=", Categoria.OperadorAsignacion,self.filaActual,self.colActual)) 
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
            if(not self.caracterActual == "="):
                self.tokens.append(Token("=", Categoria.OperadorAsignacion,self.filaActual,self.colActual)) 
                self.obtenerSiguienteCaracter()
                return True
            else:
                self.hacerBT(posInicial, filaInicial, columnaInicial)
                return False

    """
    Los operadores logicos &&, ||, !
    """
    def esOperadorLogico(self):
        
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
            self.tokens.append(Token("!", Categoria.OperadorLogico,self.filaActual,self.colActual)) 
            self.obtenerSiguienteCaracter()
            return True
        
        
        

    """
    Los operadores relacionales <,>,<=,>=,!=,== (de comparacion)
    """
    def esOperadorRelacional(self):
        
        if(self.caracterActual == '<' or self.caracterActual == '>' or self.caracterActual == '=' or self.caracterActual == '!'): #Rechazo inicial
            lexema = ""
            posicionInicial = self.posicionActual
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            
            lexema+=self.caracterActual
            self.obtenerSiguienteCaracter()
            
            if( self.caracterActual != '=') :            # Si el siguiente caracter no es = (ej. >pip <lucas =ret)
                if(self.codigo[posicionInicial] == '=' or self.codigo[posicionInicial] == '!'):    #si el caracter anterior era un = o un !
                    self.hacerBT(posicionInicial,filaInicial,columnaInicial) # hacer Bt.
                    return False
                else:
                    self.tokens.append(Token(lexema,Categoria.OperadorRelacional, self.filaActual, self.colActual))   
                    return True                             
            else:                                           #Si el segundo ch es = 
                lexema += self.caracterActual               #se captura ese = en el lexema
                self.obtenerSiguienteCaracter()             #se obt el sigte ch para continuar con el analisis
                self.tokens.append(Token(lexema, Categoria.OperadorRelacional, self.filaActual, self.colActual)) 
                return True           
        else:
            return False     

    def esNatural(self):
        
        if(self.caracterActual.isdigit()):  
            #print("es numero "+self.caracterActual)
            
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
                self.tokens.append(Token(lexema, Categoria.NumeroNatural, filaInicial, columnaInicial)) 
                return True                                 
        else:
            return False        
        
    def esReal (self):
                
        if (self.caracterActual.isdigit() or self.caracterActual == '.') :
            
            lexema = ""
            lexema += self.caracterActual
            filaInicial = self.filaActual
            columnaInicial = self.colActual
            posicionInicial = self.posicionActual
            
            if(self.caracterActual.isdigit()):
                
                self.obtenerSiguienteCaracter()
                
                while (self.caracterActual.isdigit()): 
                    lexema += self.caracterActual
                    self.obtenerSiguienteCaracter()
                
                if(not self.caracterActual == '.'):
                    self.hacerBT(posicionInicial, filaInicial, columnaInicial)
                    return False  
               
            else:
                
                self.obtenerSiguienteCaracter()
                
                if(not self.caracterActual.isdigit()):
                    self.hacerBT(posicionInicial, filaInicial, columnaInicial)     
                    return False
                   
            
            lexema += self.caracterActual # Concatenamos un punto o un digito 
            self.obtenerSiguienteCaracter()
            
            while(self.caracterActual.isdigit()):
                lexema += self.caracterActual
                self.obtenerSiguienteCaracter()
                
            
            
            self.tokens.append(Token(lexema, Categoria.NumeroReal, filaInicial, columnaInicial))
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
    

