from logica.sintactico.Expresion import Expression


class Logica(Expression):

    def __init__(self, operadorUnario, expresionLogica, expresionAuxiliarLogica, expresionRelacional):
        self.operadorUnario = operadorUnario
        self.expresionLogica = expresionLogica
        self.expresionAuxiliarLogica = expresionAuxiliarLogica
        self.expresionRelacional = expresionRelacional

    def getArbolVisual(self):
        pass