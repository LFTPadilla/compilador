
from logica.lexico.Token import Token
from logica.lexico.Categoria import Categoria
import ErrorSintactico,Parametro
from Funcion import Fun
from UnidadCompilacion import UnidadDeCompilacion


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
        if(len(listaFunciones)!=0):
            return UnidadDeCompilacion(listaFunciones)
        
        return None
    
    def obtenerSiguienteToken(self):
        self.posActual+=1
        if(self.posActual<len(self.listaTokens)):
            self.tokenActual = self.listaTokens[self.posActual]
    
    """
        <ListaFunciones> ::= <Funtion>[<ListaFunciones>]
    """
    def esListaFunciones(self):

        lista = []
        f = self.esFuncion()
        while(f!=None):
            lista.append(f)
            f = self.esFuncion()
        return lista



    """
        <Funtion> ::= fun identificador "("[<ListaParametros>]")" [":"<TipoRetorno>]<BloqueSentencias>
    """
    def esFuncion(self):#Devuelve una Function
        if(self.tokenActual.getCategoria == Categoria.PalabraReservada and self.tokenActual.getLexema() == "fun"):
            if(self.tokenActual.getCategoria() == Categoria.Identificador):
                nombre = self.tokenActual
                self.obtenerSiguienteToken();
                
                if self.tokenActual.getCategoria() == Categoria.ParentesisIzquierdo:
                    self.obtenerSiguienteToken();
                    parametros = self.esListaParametros()
                    
                    if self.tokenActual.getCategoria() == Categoria.ParentesisDerecho:
                        self.obtenerSiguienteToken()

                        if(self.tokenActual() ==Categoria.DosPuntos):
                            self.obtenerSiguienteToken()

                            retornoToken = self.esTipoRetorno()

                            self.obtenerSiguienteToken()

                            if(retornoToken==None):
                                self.reportarError("Falta especificar el tipo de retorno")

                        bloque = self.esBloqueSentencias()#BloqueSentencia 

                        if(bloque != None ):
                            return Fun(nombre,parametros,retornoToken,bloque)
                        else:
                            self.reportarError("falta Bloque sentencias")
                    else:
                        self.reportarError("Falta parentesis Derecho")
                else:
                    self.reportarError("Falta parentesis Izquierdo")
            else:
                self.reportarError("Falta nombre de funcion")
        pass

    

    """
    <TipoRetorno> ::= int | decimal | void | String | boolean | char
    """
    def esTipoRetorno(self):
        
        if(self.tokenActual.getLexema() == "int" or self.tokenActual.getLexema() == "decimal" or self.tokenActual.getLexema() == "void" or self.tokenActual.getLexema() == "String" or self.tokenActual.getLexema() == "boolean" or self.tokenActual.getLexema() == "char"):
            return self.tokenActual
        return None
    
    
    def esListaParametros(self):
        return True

    def reportarError(self,msj):
        err = error_sintactico(msj)
        self.listaErrores.append(err)

    def esBloqueSentencias(self):
        if(self.tokenActual.getCategoria() == Categoria.LlaveIzquierda):
            self.obtenerSiguienteToken()
            sentencias = self.esListaSentencias()
            if(self.tokenActual.getCategoria() == Categoria.LlaveDerecha):
                self.obtenerSiguienteToken()
                return sentencias

        return None


    def esListaSentencias(self):
        return True


    def getListaErrores(self):
        return self.listaErrores

    