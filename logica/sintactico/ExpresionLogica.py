from Expresion import Expression

class Logica(Expression):

    def __init__(self, operadorLogico, expresionRelacional):
        self.operadorLogico = operadorLogico
        self.expresionRelacional = expresionRelacional

    def getArbolVisual(self):
        pass