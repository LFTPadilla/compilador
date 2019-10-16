from Expresion import Expression

class Aritmetica(Expression):

    def __init__(self, expAritmetica, expAuxiliar, valorNumerico):
        self.expresionAritmetica = expAritmetica
        self.expresionAuxiliar = expAuxiliar
        self.valorNumerico = valorNumerico

    def getArbolVisual(self):
        
