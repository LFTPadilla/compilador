from logica.sintactico.Expresion import Expression

class AuxiliarRelacional(Expression):
    
    def __init__(self,operadorRelacional, expresionRelacional, expresionAuxiliarRelacional):
        
        self.operadorRelacional = operadorRelacional
        self.expresionRelacional = expresionRelacional
        self.expresionAuxiliar = expresionAuxiliarRelacional
    
    def construirArbol(self, arbol, n):
        pass
        