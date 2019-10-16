
from logica.lexico.Token import Token
from logica.lexico.Categoria import getCategoria

from ErrorSintactico import Error_sintactico

from UnidadCompilacion import UnidadDeCompilacion

from Funcion import Function

from Parametro import Parameter
from Argumento import Argument
from Arreglo import Array

from sentencia import Sentence
from sentenciaAsignacion import Asignacion
from sentenciaDeclararVariable import DeclaracionVariable
from sentenciaIfElse import IfElse
from sentenciaImprimir import Imprimir
from sentenciaInvocarFuncion import invocaFuncion
from sentenciaLeer import Leer
from sentenciaRetorno import Retorno
from sentenciaWhile import SentenceWhile

from expresion import expression
from ExpresionAritmetica import Aritmetica
from ExpresionAuxiliar import Auxiliar


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
       <Funcion> ::= [<visibilidad>] <TipoRetorno> Identificador "(" [<ListaParamentros>] ")" "{" <bloqueSentencias> "}"

    """
    def esFuncion(self):
        #El token de visibilidad es opcional, por eso esta en un if que de no cumplirse, no pasa nada
        if self.esVisibilidad()!=None :
            visibilidad = self.tokenActual            
            self.obtenerSiguienteToken()
        else:
            visibilidad = None    
        
        #El tipo de retorno es obligatorio    
        if self.esTipoRetorno()!=None :
            tipoRetorno = self.tokenActual
            self.obtenerSiguienteToken()
            
            #El identificador es obligatorio             
            if self.tokenActual.getCategoria == Categoria.Identificador:
                identificador = self.tokenActual
                self.obtenerSiguienteToken()
                
                #El parentesis izquierdo es obligatorio pero no se guarda
                if self.tokenActual.getCategoria() == Categoria.ParentesisIzquierdo:
                    self.obtenerSiguienteToken()
                    
                    #La lista de parametros no es obligatoria, solo se guarda de haber algo
                    parametros = self.esListaParametros()

                    #El parentesis derecho es obligario pero no se guarda
                    if(self.tokenActual().getCategoria == Categoria.ParentesisDerecho):
                        self.obtenerSiguienteToken

                        #El bloque de sentencias se guarda 
                        bloque = self.esBloqueSentencias()#BloqueSentencia 

                        if(bloque != None ): #return cuenta como sentencia y minimo debe tenerlo 
                            self.obtenerSiguienteToken
                            
                            return Funcion(visibilidad,tipoRetorno,identificador,parametros,bloque)
                        else:
                            self.reportarError("Falta Bloque sentencias", self.tokenActual.fila, self.tokenActual.columna)
                        
                    else:
                        self.reportarError("Falta parentesis Derecho", self.tokenActual.fila, self.tokenActual.columna)
                else:
                    self.reportarError("Falta parentesis izquierdo", self.tokenActual.fila, self.tokenActual.columna)
            else:
                    self.reportarError("Falta identificador de funcion", self.tokenActual.fila, self.tokenActual.columna)        
        else:
            self.reportarError("Falta tipo de retorno de la funcion", self.tokenActual.fila, self.tokenActual.columna)
    

    """
    <Visibilidad> ::= public | private | protected | default
    """
    def esVisibilidad(self):
        if(self.tokenActual.getCategoria == Categoria.PalabraReservada):        
            if(self.tokenActual.getLexema() == "public" or self.tokenActual.getLexema() == "private" or self.tokenActual.getLexema() == "protected" or self.tokenActual.getLexema() == "default"):
                return self.tokenActual
        return None

    """
    <TipoRetorno> ::= int | double | void | String | boolean | char
    """
    def esTipoRetorno(self):
        if(self.tokenActual.getCategoria == Categoria.PalabraReservada):
            if(self.tokenActual.getLexema() == "int" or self.tokenActual.lexema() == "decimal" or self.tokenActual.lexema() == "void" or self.tokenActual.lexema() == "String" or self.tokenActual.lexema() == "boolean" or self.tokenActual.lexema() == "char"):
                return self.tokenActual
        return None
    
    
    """
    <TipoDato> ::= int | String | double | boolean | char
    """
    def esTipoDato(self):
        
        if(self.tokenActual.lexema == "int" or self.tokenActual.lexema == "String" or self.tokenActual.lexema == "double" or self.tokenActual.lexema == "boolean" or self.tokenActual.lexema == "char"):
           return self.tokenActual
        return False        
    
    """
    <ListaParametros> ::= <Parametro> [","<listaParametros>]
    """
    def esListaParametros(self):
        lista = []
        f = self.esParametro()
        while(f!=None):
            lista.append(f)
            if(","): #falta la coma
                f = self.esParametro()
        return lista
        
    
    """
    <Parametro> ::= <TipoDato> identificador
    """   
    def esParametro(self):
        
        tipo_dato = self.esTipoDato()
        
        if ( not tipo_dato == False ):                                      #si el token actual es un tipo de dato
            self.obtenerSiguienteToken()
            
            if ( self.tokenActual.Categoria == Categoria.Identificador ):   #
                
                nombre = self.tokenActual
                return Parametro(tipo_dato,nombre)
            else:
                self.reportarError("No hay identificador definido para el parametro", self.tokenActual.fila, self.tokenActual.columna)
            
        else:
            self.reportarError("No hay tipo de dato definido para el parametro", self.tokenActual.fila, self.tokenActual.columna)
        
        

   

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
        s = None
        s = self.esDecision()

        if(s!=None):
            return s

        s = self.esCiclo()
        
        if(s!=None):
            return s
        
        s = self.esImpresion()

        if(s!=None):
            return s

        s = self.esLeer()
        
        if(s!=None):
            return s
        
        s = self.esAsignacionVariable()

        if(s!=None):
            return s

        s = self.esDeclaracionVariable()

        if(s!=None):
            return s

        s = self.esRetorno()

        if(s!=None):
            return s

        s = self.esInvocarMetodo()

        if(s!=None):
            return s

        s = self.esArreglo()

        if(s!=None):
            return s

        return s

    """
    <Decision>::= <sentenciaif>[<sentenciaElse>]
    """
    def esDecision(self):
        return True


    """
    <ExpresionAuxiliar>::= operadorAritmetico <ExpresionAritmetica> [<ExpresionAuxiliar>]
    """
    def esExpresionAuxiliar(self):
        if(self.tokenActual.getCategoria() == Categoria.OperadorAritmetico):
            operador = self.tokenActual
            self.obtenerSiguienteToken()
            ea = self.esExpresionAritmetica()
            if(ea != None):
                eAux = self.esExpresionAritmetica()
                return ExpresionAuxiliar(operador,ea,eAux)            
            return None
                

    """
    <ExpresionAritmetica>::= "("<ExpresionAritmetica>")"[<ExpresionAuxiliar>] | <ValorNumerico>[<ExpresionAuxiliar>]
    """
    def esExpresionAritmetica(self):

        if self.tokenActual.getCategoria() ==Categoria.ParentesisIzquierdo:
            self.obtenerSiguienteToken()
            e = self.esExpresionAritmetica()
            if(e!=None):
                if self.tokenActual.getCategoria == Categoria.ParentesisDerecho:
                    self.obtenerSiguienteToken()
                    ea = self.esExpresionAuxiliar()
                    return ExpresionAritmetica(e,ea)
        else:
            vn = self.esValorNumerico()
            if(vn == None):
                ea = self.esExpresionAuxiliar()
                return ExpresionAritmetica(vn, ea)

        return None


    """
    <ValorNumerico>::= numeroNatural | numeroReal    
    """
    def esValorNumerico(self):
        
        if(self.tokenActual.getCategoria == Categoria.NumeroNatural or self.tokenActual.getCategoria == Categoria.NumeroReal):
            return self.tokenActual
        return None



    """
    <SentenciaIf>::= if "(" <ExpresionLogica> ")" <BloqueSentencia>
    """
    def esSentenciaIf(self):
        return True #se puso true, para que no arroje error su declaracionen el metodo esSentencia, es None

    """
    <SentenciaElse>::= else <BloqueSentencia>
    """
    def esSentenciaElse(self):
        return True #se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <DeclaracionVariable>::= 
    """
    def esDeclaracionVariable(self):
        return True#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <AsignacionVariable>::= 
    """
    def esAsignacionVariable(self):
        return True#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <Imprimir>::= imprimir "(" [<expresion>] ")" ";"
    """
    def esImprimir(self):
        return True#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <Leer>::= leer "(" [<expresion>] ")" ";"
    """
    def esLeer(self):
        return True#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <Ciclo>::= while "(" <expresionLogica> ")" <bloqueSentencia>
    """
    def esCiclo(self):
        return True#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <Retorno>::= retorno identificador ";"
    """
    def esRetorno(self):
        return True#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <InvocarMetodo>::= invocar identificador "(" <ListaArgumentos> ")" ";"
    """
    def esInvocarMetodo(self):
        return True#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <ListaArgumentos>::= <Argumento>["," <ListaArgumentos>]
    """
    def esListaArgumentos(self):

        lista = []
        f = self.esArgumento()
        while(f!=None):
            lista.append(f)
            if(","): #falta la coma
                f = self.esArgumento()
        return lista


    """
    <Argumento>::= identificador | <expresion>
    """
    def esArgumento(self):
        return True
    
    """
    <Arreglo>::= 
    """
    def esArreglo(self):
        return True 
    
    """
    <Impresion>::= 
    """
    def esImpresion(self):
        return True 

    def getListaErrores(self):
        return self.listaErrores

    