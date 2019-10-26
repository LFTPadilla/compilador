from logica.sintactico.Expresion import Expression


class AuxiliarLogica(Expression):
    
    def __init__(self,operadorLogico,expresionRelacional):
        
        self.operadorLogico = operadorLogico
        self.expresionRelacional = expresionRelacional
    
    def construirArbol(self, arbol):
        
        arbol.setText(0,self.operadorLogico.lexema+" "+(str)(self.expresionRelacional) )
        