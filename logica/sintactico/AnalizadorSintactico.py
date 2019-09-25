

class ASintactico: 
    listaTokens = []
    posActual = 0
    listaErrores = []

    def __init__(self,listaTokens):
        self.listaTokens = listaTokens
        self.tokenActual = self.listaTokens[self.posActual]


    """
        <UnidadDeCompilacion> ::= <ListaFunciones>
    """
    def esUnidadDeCompilacion(self):
        listaFunciones = self.esListaFunciones()
        return UnidadDeCompilacion(listaFunciones)
    
    def obtenerSiguienteToken():
        self.posActual++
        if(self.posActual<len(self.listaTokens)):
            self.tokenActual = self.listaTokens[self.posActual]
    
    """
        <ListaFunciones> ::= <Funtion>[<ListaFunciones>]
    """
    def esListaFunciones(self):
        Funtion f = self.esFuncion()
        return 


    """
        <Funtion> ::= fun identificador "("[<ListaParametros>]")" [":"<TipoRetorno>]<BloqueSentencias>
    """
    def Funtion esFuncion(self):
        if(self.tokenActual.getCategoria == Categoria.PALABRA_RESERVADA && self.tokenActual.getLexema() == "fun"):
            if(self.getCategoria() == Categoria.IDENTIFICADOR):
                Token nombre = self.tokenActual
                self.obtenerSiguienteToken();
                
                if self.tokenActual.getCategoria() == Categoria.PARENTESIS_IZQUIERDO:
                    self.obtenerSiguienteToken();
                    parametros = esListaParametros()
                    
                    if self.tokenActual.getCategoria() == Categoria.PARENTESIS_DERECHO:
                        self.obtenerSiguienteToken();

                        if(self.tokenActual() ==Categoria.DOS_PUNTOS):
                            pass

                        BloqueSentencia bloque = esBloqueSentencias()

                        if(bloque!=null):
                            return Funcion(nombre, parametros, TipoRetorno, bloque)
            else:
                self.reportarError("Falta nombre de funcion");
        pass


    def reportarError(self,msj):
        err = ErrorSintactico(msj)
        self.listaErrores.append(err)