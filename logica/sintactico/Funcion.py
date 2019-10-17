class Function:

    def __init__(self, visibilidad, retorno, identificador, parametros, bloque):
        self.visibilidad = visibilidad
        self.identificador = identificador
        self.parametros = parametros
        self.retorno = retorno
        self.bloque ="""
    <ExpresionRelacional>::= "("<ExpresionRelacional>")"[<ExpresionAuxiliarRela>] | <Termino> [<ExpresionAuxiliarRela>]
    """
    def esExpresionRelacional(self):   
        
        if self.tokenActual.getCategoria == Categoria.ParentesisIzquierdo :
            
            self.obtenerSiguienteToken()
            
            er = esExpresionRelacional()
            
            if er != None :
                 self.obtenerSiguienteToken()
                 
                 if self.tokenActual.getCategoria == Categoria.ParentesisDerecho :
                     
                     self.obtenerSiguienteToken()
                     ear = ExpresionAuxiliarRelacional(er,ear,None)
                     
                     return 
                     
                
    
    """
    <ExpresionAuxiliarRelacional>::= operadorRelacional <ExpresionRelacional>[<ExpresionAuxiliarRelacional>]
    """
    def esExpresionAuxiliarRelacional(self): bloque

    def __repr__(self):
        return "(Funcion: visibilidad: %s, identificador: %s, parametros: %s, retorno: %s, bloqueSentencias: %s)" % (self.visibilidad, self.identificador, self.parametros, self.retorno, self.bloque)

    def __str__(self):
        return "Funcion [%s, %s, %s, %s, %s]"% (self.visibilidad, self.identificador, self.parametros, self.retorno, self.bloque)