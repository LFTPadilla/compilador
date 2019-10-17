from Expresion import Expression

class Logica(Expression):

    def __init__(self, cadenaCaracteres, expresion):
        self.cadenaCaracteres = cadenaCaracteres
        self.expresion = expresion

    def getArbolVisual(self):