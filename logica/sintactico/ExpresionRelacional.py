from Expresion import Expression

class Relacional(Expression):

    def __init__(self, expRelacional, expAuxiliarRelacional, valorNumerico):
        self.expresionRelacional = expRelacional
        self.expresionAuxiliarRelacional = expAuxiliarRelacional
        self.valorNumerico = valorNumerico

    def getArbolVisual(self):
        pass