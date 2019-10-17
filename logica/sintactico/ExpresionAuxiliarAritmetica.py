from Expresion import Expression

class AuxiliarAritmetica(Expression):
    
    def __init__(self,operadorAritmetico, expresionAritmetica, expresionAuxiliarAritmetica):
        
        self.operadorAritmetico = operadorAritmetico
        self.expresionAritmetica = expresionAritmetica
        self.expresionAuxiliar = expresionAuxiliarAritmetica
    
    def getArbolVisual(self):
        pass
        