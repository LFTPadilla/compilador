from Expresion import Expression

class Auxiliar(Expression):
    
    def __init__(self,operadorAritmetico,expresionAritmetica,expresionAuxiliar):
        
        self.operadorAritmetico = operadorAritmetico
        self.expresionAritmetica = expresionAritmetica
        self.expresionAuxiliar = expresionAuxiliar
    
    def getArbolVisual(self):
        pass
        