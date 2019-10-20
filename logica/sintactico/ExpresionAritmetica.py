from compilador.logica.sintactico.Expresion import Expression

class Aritmetica(Expression):

    def __init__(self, expAritmetica, expAuxiliarAritmetica, valorNumerico):
        self.expresionAritmetica = expAritmetica
        self.expresionAuxiliar = expAuxiliarAritmetica
        self.valorNumerico = valorNumerico

    def getArbolVisual(self):
        pass
