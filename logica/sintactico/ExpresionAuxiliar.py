from Expresion import Exp

class ExpresionAuxiliar(Exp):
    
    def __init__(self,operadorAritmetico,expresionAritmetica,expresionAuxiliar):
        
        self.operadorAritmetico = operadorAritmetico
        self.expresionAritmetica = expresionAritmetica
        self.expresionAuxiliar = expresionAuxiliar
        