from logica.sintactico.Expresion import Expression


class Cadena(Expression):

    def __init__(self, cadenaCaracteres, expresion):
        self.cadenaCaracteres = cadenaCaracteres
        self.expresion = expresion

    def construirArbol(self, arbol, n):
        pass