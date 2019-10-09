
from logica.lexico.Token import Token
from logica.lexico.Categoria import Categoria
import ErrorSintactico,Parametro
from Funcion import Fun
from UnidadCompilacion import UnidadDeCompilacion
from ErrorSintactico import error_sintactico

class ASintactico: 
    listaTokens = []
    posActual = 0
    listaErrores = []

    def __init__(self,listaTokens):
        self.listaTokens = listaTokens
        self.tokenActual = self.listaTokens[self.posActual]

    def reportarError(self,msj,f,c):
        err = error_sintactico(msj,f,c)
        self.listaErrores.append(err)

    def obtenerSiguienteToken(self):
        self.posActual+=1
        if(self.posActual<len(self.listaTokens)):
            self.tokenActual = self.listaTokens[self.posActual]

    """
        <UnidadDeCompilacion> ::= <ListaFunciones>
    """
    def esUnidadDeCompilacion(self):
        listaFunciones = self.esListaFunciones()
        if(len(listaFunciones)!=0):
            return UnidadDeCompilacion(listaFunciones)
        
        return None
    
    """
        <ListaFunciones> ::= <Funcion>[<ListaFunciones>]
    """
    def esListaFunciones(self):

        lista = []
        f = self.esFuncion()
        while(f!=None):
            lista.append(f)
            f = self.esFuncion()
        return lista

    """
        <Funcion> ::= fun identificador "("[<ListaParametros>]")" [":"<TipoRetorno>]<BloqueSentencias>

        CAMBIAAAR OJO 

        <Funcion> ::= [<visibilidad>] <TipoRetorno> Identificador "(" [<ListaParamentros>] ")" <bloqueSentencia>

    """
    def esFuncion(self):#Devuelve una Function
        if(self.tokenActual.getCategoria == Categoria.PalabraReservada and self.tokenActual.getLexema() == "funcion"):
            self.obtenerSiguienteToken()
            if(self.tokenActual.getCategoria() == Categoria.Identificador):
                nombre = self.tokenActual
                self.obtenerSiguienteToken()
                                
                if self.tokenActual.getCategoria() == Categoria.ParentesisIzquierdo:
                    self.obtenerSiguienteToken()
                    parametros = self.esListaParametros()
                    
                    if self.tokenActual.getCategoria() == Categoria.ParentesisDerecho:
                        self.obtenerSiguienteToken()

                        if(self.tokenActual() ==Categoria.DosPuntos):
                            self.obtenerSiguienteToken()

                            retornoToken = self.esTipoRetorno()

                            self.obtenerSiguienteToken()

                            if(retornoToken==None):
                                self.reportarError("Falta especificar el tipo de retorno",self.tokenActual.fila, self.tokenActual.columna)

                        bloque = self.esBloqueSentencias()#BloqueSentencia 

                        if(bloque != None ):
                            return Fun(nombre,parametros,retornoToken,bloque)
                        else:
                            self.reportarError("falta Bloque sentencias", self.tokenActual.fila, self.tokenActual.columna)
                    else:
                        self.reportarError("Falta parentesis Derecho", self.tokenActual.fila, self.tokenActual.columna)
                else:
                    self.reportarError("Falta parentesis Izquierdo", self.tokenActual.fila, self.tokenActual.columna)
            else:
                self.reportarError("Falta nombre de funcion", self.tokenActual.fila, self.tokenActual.columna)
        pass

    """
    <Visibilidad> ::= public | private | protected | default
    """
    def esVisibilidad(self):
        
        if(self.tokenActual.getLexema() == "public" or self.tokenActual.getLexema() == "private" or self.tokenActual.getLexema() == "protected" or self.tokenActual.getLexema() == "default"):
            return self.tokenActual
        return None

    """
    <TipoRetorno> ::= int | double | void | String | boolean | char
    """
    def esTipoRetorno(self):
        
        if(self.tokenActual.getLexema() == "int" or self.tokenActual.getLexema() == "double" or self.tokenActual.getLexema() == "void" or self.tokenActual.getLexema() == "String" or self.tokenActual.getLexema() == "boolean" or self.tokenActual.getLexema() == "char"):
            return self.tokenActual
        return None
    
    """
        <ListaParametros> ::= <Parametro>[","<ListaParametros>]
    """
    def esListaParametros(self):

        lista = []
        f = self.esParametro()
        while(f!=None):
            lista.append(f)
            if(",") falta la coma
            f = self.esParametro()
        return lista

    """
    <Parametro> ::= <TipoRetorno> identificador
    """
    def esParametro(self):
        
        return None

    """
        <BloqueSentencia> ::= "{" [<listaSentencias>] "}"
    """
    def esBloqueSentencias(self):
        if(self.tokenActual.getCategoria() == Categoria.LlaveIzquierda):
            self.obtenerSiguienteToken()
            sentencias = self.esListaSentencias()
            if(self.tokenActual.getCategoria() == Categoria.LlaveDerecha):
                self.obtenerSiguienteToken()
                return sentencias

        return None

    """
        <ListaSentencias> ::= <sentencia>[<listaSentencias>]
    """
    def esListaSentencias(self):
        
        lista = []
        f = self.esSentencia()
        while(f!=None):
            lista.append(f)
            f = self.esSentencia()
        return lista

    """
    <sentencia> ::= <Desicion> | <ciclo> | <Impresion> | <lectura> | <Asignacion> | <declaracionVariable> |
                    <retorno> | <invocaFuncion> | <arreglo>
    """
    def esSentencia(self):
        Sentencia s = None;
        s = esDecision()

        if(s!=None):
            return s

        s = esCiclo()
        
        if(s!=None):
            return s
        
        s = esImpresion()

        if(s!=None):
            return s

        s = esLeer()
        
        if(s!=None):
            return s
        
        s = esAsignacionVariable()

        if(s!=None):
            return s

        s = esDeclaracionVariable()

        if(s!=None):
            return s

        s = esRetorno()

        if(s!=None):
            return s

        s = esInvocarMetodo()

        if(s!=None):
            return s

        s = esArreglo()

        if(s!=None):
            return s

        return s

    """
    <Decision>::= <sentenciaif>[<sentenciaElse>]
    """
    def esDecision(self):
        return None

    def esExpresionAuxiliar(self):
        if(self.tokenActual.getCategoria() == Categoria.OperadorAritmetico):
            operador = self.tokenActual;
            self.obtenerSiguienteToken()
            ea = esExpresionAritmetica(); 
            if(ea != None):
                eAux = esExpresionAritmetica()
                return ExpresionAritmetica()
                


    def esExpresionAritmetica(self):

        if self.tokenActual.getCategoria() ==Categoria.ParentesisIzquierdo:
            self.obtenerSiguienteToken()
            e = ExpresionArimetica()
            if(e!=null):
                if self.tokenActual.getCategoria == Categoria.ParentesisDerecho:
                    self.obtenerSiguienteToken()
                    ea = esExpresionAuxiliar();
                    return ExpresionArimetica(e,ea)
        else:
            valorNumerico = esValorNumerico();
            if(valorNumerico == None):
                ea = esExpresionAuxiliar()
                return ExpresionAritmetica(vn, ea)

        return None

    """
    <SentenciaIf>::= if "(" <ExpresionLogica> ")" <BloqueSentencia>
    """
    def esSentenciaIf(self):
        return None

    """
    <SentenciaElse>::= else <BloqueSentencia>
    """
    def esSentenciaElse(self):
        return None

    """
    <DeclaracionVariable>::= 
    """
    def esDeclaracionVariable(self):
        return None

    """
    <AsignacionVariable>::= 
    """
    def esAsignacionVariable(self):
        return None

    """
    <Imprimir>::= imprimir "(" [<expresion>] ")" ";"
    """
    def esImprimir(self):
        return None

    """
    <Leer>::= leer "(" [<expresion>] ")" ";"
    """
    def esLeer(self):
        return None

    """
    <Ciclo>::= while "(" <expresionLogica> ")" <bloqueSentencia>
    """
    def esCiclo(self):
        return None

    """
    <Retorno>::= retorno identificador ";"
    """
    def esRetorno(self):
        return None

    """
    <InvocarMetodo>::= invocar identificador "(" <ListaArgumentos> ")" ";"
    """
    def esInvocarMetodo(self):
        return None

    """
    <ListaArgumentos>::= <Argumento>["," <ListaArgumentos>]
    """
    def esListaArgumentos(self):

        lista = []
        f = self.esArgumento()
        while(f!=None):
            lista.append(f)
            if(",") falta la coma
            f = self.esArgumento()
        return lista


    """
    <Arreglo>::= 
    """
    def esArreglo(self):
        return None

    def getListaErrores(self):
        return self.listaErrores

    