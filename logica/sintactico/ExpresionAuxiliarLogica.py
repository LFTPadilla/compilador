from compilador.logica.sintactico.Expresion import Expression


class AuxiliarLogica(Expression):
    
    def __init__(self,operadorBinario, expresionLogica, expresionAuxiliarLogica):
        
        self.operadorBinario = operadorBinario
        self.expresionLogica = expresionLogica
        self.expresionAuxiliarLogica = expresionAuxiliarLogica
    
    def getArbolVisual(self):
        pass
        