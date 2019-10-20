from compilador.logica.sintactico.Expresion import Expression


class Relacional(Expression):

    def __init__(self, expRelacional, expAuxiliarRelacional, termino):
        self.expresionRelacional = expRelacional
        self.expresionAuxiliarRelacional = expAuxiliarRelacional
        self.termino = termino

    def getArbolVisual(self):
        pass