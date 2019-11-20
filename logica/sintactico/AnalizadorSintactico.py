from logica.lexico.Categorias import Categoria
from logica.lexico.Tokens import Token

from PyQt5 import QtWidgets

from logica.sintactico.UnidadCompilacion import UnidadComp
from logica.sintactico.Error import errorSintactico
from logica.sintactico.Funcion import Function

from logica.sintactico.Argumento import Argument
from logica.sintactico.Parametro import Parameter
from logica.sintactico.Arreglo import Array

from logica.sintactico.BloqueSentencias import bloqueSent

from logica.sintactico.Sentencia import Sentence
from logica.sintactico.SentenciaAsignacion import Asignacion
from logica.sintactico.SentenciaDeclararVariable import DeclaracionVariable
from logica.sintactico.SentenciaDecision import Decision
from logica.sintactico.SentenciaImprimir import Imprimir
from logica.sintactico.SentenciaInvocarFuncion import InvocarFuncion
from logica.sintactico.SentenciaLeer import Leer
from logica.sintactico.SentenciaRetorno import Retorno
from logica.sintactico.SentenciaWhile import SentenceWhile
from logica.sintactico.SentenciaIncrementoDecremento import IncrementoDecremento

from logica.sintactico.Expresion import Expression
from logica.sintactico.ExpresionAritmetica import Aritmetica 
from logica.sintactico.ExpresionCadena import Cadena
from logica.sintactico.ExpresionLogica import Logica
from logica.sintactico.ExpresionRelacional import Relacional

from logica.sintactico.ExpresionAuxiliarAritmetica import AuxiliarAritmetica
from logica.sintactico.ExpresionAuxiliarLogica import AuxiliarLogica

from logica.sintactico.Mapa import mapita
from logica.sintactico.ComponenteMapa import componenteMap

from logica.sintactico.SentenciaIF import SentIF
from logica.sintactico.SentenciaELSE import SentELSE

from logica.semantica.AnalizadorSemantico import ASemantico

class ASintactico: 
    
    unidadCompilacion = None

    def __init__(self,listaTokens,arbol):
        self.arbol = arbol
        self.posActual = 0
        self.listaTokens = listaTokens
        self.tokenActual = self.listaTokens[self.posActual]
        self.palabrasReservadas = ["String","abstract","continue","for","new","switch","assert","default","goto","package","synchronized","boolean","do","if","private","this","break","double","implements","protected","throw","byte","else","import","public","throws","case","enum","instanceof","return","transient","catch","extends","int","short","try","char","final","interface","static","void","class","finally","long","strictfp","volatile","const","float","native","super","while","map", "array" "let", "asig"]        
        self.listaErrores = []
        

    def reportarError(self,msj,fila,columna):
        err = errorSintactico(msj,fila,columna)
        self.listaErrores.append(err)

    def obtenerSiguienteToken(self):
        self.posActual+=1
        if(self.posActual<len(self.listaTokens)):
            self.tokenActual = self.listaTokens[self.posActual]

    def hacerBT(self, posToken):
        self.posActual = posToken
        self.tokenActual = self.listaTokens[posToken]

    """
        <UnidadDeCompilacion> ::= <ListaFunciones>
    """
    def esUnidadDeCompilacion(self):
        listaFunciones = self.esListaFunciones()
        if(len(listaFunciones)!=0):
            self.unidadCompilacion = UnidadComp(listaFunciones)
            return self.unidadCompilacion
        return None

    

    """
        <ListaFunciones> ::= <Funcion>[<ListaFunciones>]
    """
    def esListaFunciones(self):
        lista = []
        contador = 0
        f = self.esFuncion(contador)
        while f != None:
            lista.append(f)
            contador += 1
            f = self.esFuncion(contador)
        return lista

    """
       <Funcion> ::= [<visibilidad>] <TipoRetorno> Identificador "(" [<ListaParametros>] ")" <bloqueSentencias>
    """
    def esFuncion(self, contador):
        if self.posActual < len(self.listaTokens):
            #El token de visibilidad es opcional, por eso esta en un if que de no cumplirse, no pasa nada
            visibilidad  = self.esVisibilidad()
                
            #El tipo de retorno es obligatorio  
            tipoRetorno = self.esTipoRetorno()  

            if tipoRetorno!=None :
                #El identificador es obligatorio             
                if self.tokenActual.categoria == Categoria.Identificador:
                    identificador = self.tokenActual

                    self.obtenerSiguienteToken()

                    #El parentesis izquierdo es obligatorio pero no se guarda
                    if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:

                        self.obtenerSiguienteToken()

                        #La lista de parametros no es obligatoria, solo se guarda de haber algo
                        parametros = self.esListaParametros()   

                        #El parentesis derecho es obligario pero no se guarda
                        if(self.tokenActual.categoria == Categoria.ParentesisDerecho):

                            self.obtenerSiguienteToken()

                            #El bloque de sentencias se guarda 
                            bloque = self.esBloqueSentencias()#BloqueSentencia 
                            
                            if bloque != None: #return cuenta como sentencia y minimo debe "{" "}"
                        
                                funcion = Function(visibilidad,tipoRetorno,identificador,parametros,bloque)

                                funcion.construirArbol(self.arbol,contador)

                                return funcion
                            else:
                                self.reportarError("Falta Bloque sentencias en la funcion", self.tokenActual.fila, self.tokenActual.columna)   
                        else:
                            self.reportarError("Falta parentesis Derecho en la funcion", self.tokenActual.fila, self.tokenActual.columna)
                    else:
                        self.reportarError("Falta parentesis izquierdo en la funcion", self.tokenActual.fila, self.tokenActual.columna)
                else:
                    self.reportarError("Falta identificador de funcion", self.tokenActual.fila, self.tokenActual.columna)        
            else:
                self.reportarError("Falta tipo de retorno de la funcion", self.tokenActual.fila, self.tokenActual.columna)
            return None
        return None

    """
        <Visibilidad> ::= public | private | protected | default
    """
    def esVisibilidad(self):
        if(self.tokenActual.categoria == Categoria.PalabraReservada):
            if(self.tokenActual.lexema == "public" or self.tokenActual.lexema == "private" or self.tokenActual.lexema == "protected" or self.tokenActual.lexema == "default"):
                visibilidad = self.tokenActual
                self.obtenerSiguienteToken()        
                return visibilidad
        return None

    """
        <TipoRetorno> ::= int | String | double | boolean | char | void
    """
    def esTipoRetorno(self):
        if self.tokenActual.categoria == Categoria.PalabraReservada:
            if self.tokenActual.lexema == "int" or self.tokenActual.lexema == "String" or self.tokenActual.lexema == "double" or self.tokenActual.lexema == "boolean" or self.tokenActual.lexema == "char" or self.tokenActual.lexema == "void":
                tipoRetorno = self.tokenActual
                self.obtenerSiguienteToken()
                return tipoRetorno
            else:
                self.reportarError("No es un TipoRetorno valido", self.tokenActual.fila, self.tokenActual.columna)
        return None
    
    """
        <TipoDato> ::= int | String | double | boolean | char
    """
    def esTipoDato(self):
        if self.tokenActual.categoria == Categoria.PalabraReservada and (self.tokenActual.lexema == "int" or self.tokenActual.lexema == "String" or self.tokenActual.lexema == "double" or self.tokenActual.lexema == "boolean" or self.tokenActual.lexema == "char") :
            tipoDato = self.tokenActual
            self.obtenerSiguienteToken()
            return tipoDato
        return None        
    
    """
        <ListaParametros> ::= <Parametro> [","<listaParametros>]
    """
    def esListaParametros(self):

        # Se inicializa la lista de parametros
        listaParametros = []

        contador = 0

        # obligatoriamente debe de existir un parametro
        parametro = self.esParametro(contador)

        while parametro != None:

                # se agrega parametro actual
                listaParametros.append(parametro)

                contador += 1
                # despues de ser agregado a la lista se vuelve nulo para hallar uno nuevo
                parametro = None
                
                # se pregunta si sigue un separador para agregar un nuevo parametro
                if self.tokenActual.categoria == Categoria.Separador:
                    self.obtenerSiguienteToken()

                    # se busca un nuevo parametro
                    parametro = self.esParametro(contador)

                    # el parametro no puede se None
                    if parametro == None:
                        self.reportarError("despues de la coma no se encontro un parametro valido", self.tokenActual.fila, self.tokenActual.columna)

        # se retorna la lista de argumentos del mapa
        return listaParametros
        
    """
        <Parametro> ::= <TipoDato> identificador
    """   
    def esParametro(self, contador):
        if self.tokenActual.categoria != Categoria.ParentesisDerecho:
            tipo_dato = self.esTipoDato()
            if  not tipo_dato == False :  #si el token actual es un tipo de dato
                if ( self.tokenActual.categoria == Categoria.Identificador ):   #
                    
                    nombre = self.tokenActual
                    self.obtenerSiguienteToken()

                    Parametro = Parameter(tipo_dato,nombre)

                    #Parametro.construirArbol(self.funcion, contador)

                    return Parametro
                else:
                    self.reportarError("No hay identificador definido para el parametro", self.tokenActual.fila, self.tokenActual.columna)
            else:
                self.reportarError("No hay tipo de dato definido para el parametro", self.tokenActual.fila, self.tokenActual.columna)
        return None
        
    """
        <BloqueSentencia> ::= "{" [<listaSentencias>] "}"
    """
    def esBloqueSentencias(self):

        if(self.tokenActual.categoria == Categoria.LlaveIzquierda):
            self.obtenerSiguienteToken()

            sentencias = self.esListaSentencias()
            
            if(self.tokenActual.categoria == Categoria.LlaveDerecha):

                self.obtenerSiguienteToken()
                return bloqueSent (sentencias)
            else:
                self.reportarError("Falta la llave derecha en el bloque de sentencias", self.tokenActual.fila, self.tokenActual.columna)
        else:
            self.reportarError("Falta la llave izquierda en el bloque de sentencias", self.tokenActual.fila, self.tokenActual.columna)        
        return None

    """
        <ListaSentencias> ::= <sentencia> [<listaSentencias>]
    """
    def esListaSentencias(self):
        
        lista = []
        contador = 0
        f = self.esSentencia(contador)
        while(f!=None):
            lista.append(f)
            f = self.esSentencia(contador)
        return lista

    """
    <sentencia> ::= <Desicion> | <ciclo> | <Impresion> | <lectura> | <Asignacion> | <declaracionVariable> |
                    <retorno> | <invocaFuncion> | <arreglo> | <mapa>
    """
    def esSentencia(self, contador):
        
        if self.tokenActual.categoria != Categoria.LlaveDerecha:

            s = None

            s = self.esDecision() #Falla
            if(s!=None):
                return s

            s = self.esCiclo()
            
            if(s!=None):
                return s
            
            s = self.esImprimir()

            if(s!=None):
                return s

            s = self.esLeer()
            
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

            s = self.esIncrementoDecremento()
            
            if(s!=None):
                return s

            
            s = self.esArreglo()

            if(s!=None):
                return s

            s = self.esMapa()

            if(s!=None):
                return s

            s = self.esAsignacionVariable()

            if(s!=None):
                return s
            
            if s == None:
                self.reportarError("La sentencia es invalida", self.tokenActual.fila, self.tokenActual.columna)

            contador += 1

            return s

        return None

    """
    <Expresion>::= <ExpresionAritmetica> | <ExpresionLogica> |<ExpresionRelacional> |<ExpresionCadena>
    """
    def esExpresion(self):
        
        e = None
        
        posToken = self.posActual
        
        e = self.esExpresionLogica()
                
        if e != None:
            return e
        else:
            self.hacerBT(posToken)
        
        posToken = self.posActual
        e = self.esExpresionAritmetica()
        
        if e != None :
            return e
        else:
            self.hacerBT(posToken)
                    
        e = self.esExpresionCadena()
        
        if e != None:
            return e

        return None
             
    """
    <ExpresionAritmetica>::= "("<ExpresionAritmetica>")"[<ExpresionAuxiliarAritmetica>] | <Termino>[<ExpresionAuxiliarAritmetica>]
    """
    def esExpresionAritmetica(self):
        
        termino = self.esTermino() #capturamos si es termino desde aca, ya que si se pone en eset if, luego el token actual se veria desplazado y mas abajo se necesita saber si es termino o no
        if self.tokenActual.categoria == Categoria.ParentesisIzquierdo or termino !=None : 
            if self.tokenActual.categoria ==Categoria.ParentesisIzquierdo:
                
                self.obtenerSiguienteToken()
                e = self.esExpresionAritmetica()

                if(e!=None):

                    if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                        self.obtenerSiguienteToken()

                        ea = self.esExpresionAuxiliarAritmetica()

                        return Aritmetica(e,ea, None)
                    else:
                        self.reportarError("Falta el parentesis de cierre en la expresion aritmetica",self.tokenActual.fila,self.tokenActual.columna)
                else:
                    self.reportarError("No hay una expresion aritmetica valida", self.tokenActual.fila,self.tokenActual.columna)
            else:
                
                
                if(termino != None): #si solo es un termino, ya estamos obteniendo el siguiente token en esTermino()
                    ea = self.esExpresionAuxiliarAritmetica()

                    return Aritmetica(None, ea , termino)
                else:
                    self.reportarError("No hay un termino valido", self.tokenActual.fila, self.tokenActual.columna)
        return None

    """
    <ExpresionAuxiliarAritmetica>::= operadorAritmetico <ExpresionAritmetica> [<ExpresionAuxiliar>]
    """
    def esExpresionAuxiliarAritmetica(self):

        if(self.tokenActual.categoria == Categoria.OperadorAritmetico):
            operador = self.tokenActual

            self.obtenerSiguienteToken()
            
            ea = self.esExpresionAritmetica()

            if(ea != None):

                eAux = self.esExpresionAuxiliarAritmetica()
                return AuxiliarAritmetica(operador,ea,eAux)      

            else: 
                self.reportarError("despues del operador aritmetico no existe una expresion aritmetica valida", self.tokenActual.fila, self.tokenActual.columna)               
        return None       
        
    """
    <ExpresionRelacional>::= <ExpresionAritmetica> operadorRelacional <ExpresionAritmetica> |
    """
    def esExpresionRelacional(self):      

        esArit =  self.esExpresionAritmetica()
        
        if esArit !=None:
            
            if(self.tokenActual.categoria == Categoria.OperadorRelacional):
                
                opRelaciona = self.tokenActual
                self.obtenerSiguienteToken()
                esArit2 =  self.esExpresionAritmetica()
                if esArit2 !=None:
                    return Relacional(esArit,opRelaciona,esArit2) 
                    
                else:
                    self.reportarError("No hay expresion aritmetica segundaria", self.tokenActual.fila, self.tokenActual.columna)               
                    return None
            else:
                return None
        return None
        
       
             
    """
    <Termino>::= <ValorNumerico> | identificador
    """    
    def esTermino(self):
        
        if(self.esValorNumerico() != None or self.tokenActual.categoria == Categoria.Identificador):
            termino = self.tokenActual
            self.obtenerSiguienteToken()
            return termino
        return None

    """
    <ValorNumerico>::= numeroNatural | numeroReal    
    """
    def esValorNumerico(self):
        
        if(self.tokenActual.categoria == Categoria.NumeroNatural or self.tokenActual.categoria == Categoria.NumeroReal):
            return self.tokenActual
        return None

    """
    <ExpresionCadena>::= cadena [ "," <listaExpresiones> ] 
    """
    def esExpresionCadena(self):
        
        if self.tokenActual.categoria == Categoria.CadenaCaracteres :
            cadena = self.tokenActual
            
            self.obtenerSiguienteToken()    
            
            if self.tokenActual.lexema == ",":
                
                self.obtenerSiguienteToken()

                e = self.esListaExpresiones()

                
                if len(e)>0:
                    
                    return Cadena(cadena, e)                
                else:
                    self.reportarError("Mal concatenado", self.tokenActual.fila, self.tokenActual.columna)
            else:
                listvacia =  []
                return Cadena(cadena,listvacia)
        else:
            return None        
    """
    <ExpresionLogica>::=    
    "!" "(" <ExpresionLogica> ")" [operadorLogico <ExpresionLogica>] [<ExpresionAuxiliarLogica>]
    | "(" <ExpresionLogica> operadorLogicoBinario <ExpresionLogica> ")" operadorLogicoBinario <ExpresionLogica> [<ExpresionAuxiliarLogica>] 
    | <ExpresionRelacional> [<ExpresionAuxiliarLogica>]                         
    """
    def esExpresionLogica(self):
        
        posicionInicial = self.posActual
        
        er = self.esExpresionRelacional()
        if er != None: 
            eal = self.esExpresionAuxiliarLogica()
            return Logica(None,None,None,None,None,er,eal)
        else:
            self.hacerBT(posicionInicial)
        
        if self.tokenActual.lexema == "!":
            operador1 = self.tokenActual
            self.obtenerSiguienteToken()
            
            if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:
                self.obtenerSiguienteToken()
                
                el1 = self.esExpresionLogica()
                if el1 != None:
                    if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                        self.obtenerSiguienteToken()
                        operador2 = self.esOperadorLogicoBinario()
                        el2 = self.esExpresionLogica()
                        eal = self.esExpresionAuxiliarLogica()
                        
                        return Logica(operador1,el1,operador2,el2,None,None,eal)
                        
                    else:
                        self.reportarError("No hay cierre de parentesis", self.tokenActual.fila, self.tokenActual.columna)
                        return None
                else:
                    self.reportarError("No hay una expresion logica valida para negar", self.tokenActual.fila, self.tokenActual.columna)
                    return None
            else:
                self.reportarError("No hay parentesis izquierdo", self.tokenActual.fila, self.tokenActual.columna)
                return None
        
        if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:
            
            self.obtenerSiguienteToken()
            el1 = self.esExpresionLogica()
            if el1 != None:
                operador1 = self.esOperadorLogicoBinario()
                if operador1 != None:
                    
                    el2 = self.esExpresionLogica()
                    if el2 != None:
                        if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                            self.obtenerSiguienteToken()
                            operador2 = self.esOperadorLogicoBinario()
                            
                            if operador2 != None:
                                el3 = self.esExpresionLogica()
                                if el3 != None:
                                    eal = self.esExpresionAuxiliarLogica()
                                    
                                    return Logica(operador1,el1,operador2,el2,el3,None,eal)
                                else:
                                    self.reportarError("No hay una expresion logica valida ", self.tokenActual.fila, self.tokenActual.columna)
                                    return None
                            else:
                                self.reportarError("No hay un operador logico valido ", self.tokenActual.fila, self.tokenActual.columna)
                                return None
                        else:
                            self.reportarError("No hay Parentesis derecho ", self.tokenActual.fila, self.tokenActual.columna)
                            return None
                    else:
                        self.reportarError("No hay una expresion logica valida ", self.tokenActual.fila, self.tokenActual.columna)
                        return None
                else:
                    self.reportarError("No hay un operador logico valido ", self.tokenActual.fila, self.tokenActual.columna)
                    return None
            else:
                #self.reportarError("No hay una expresion logica valida ", self.tokenActual.fila, self.tokenActual.columna)
                return None
        
        return None 
        
        
                                                                        
                
               
    """
    <EsOperadorLogicoBinario>::= && | ||
    """
    def esOperadorLogicoBinario(self):
        
        if self.tokenActual.lexema == "&&" or self.tokenActual.lexema == "||":
            op = self.tokenActual
            self.obtenerSiguienteToken()
            return op
        else:
            return None              
                
            
        
        
        
        
        
        
       
    

    """
    <ExpresionAuxiliarLogica> ::= operadorLogico <ExpresionLogica> [ <ExpresionLogica> ]
    """
    def esExpresionAuxiliarLogica(self):

        posicionInicial = self.posActual
        operador = self.esOperadorLogicoBinario()
        if operador != None:
            
            self.obtenerSiguienteToken()
            esLogico = self.esExpresionLogica()

            if esLogico != None:
                auxiliar  = self.esExpresionAuxiliarLogica()
                return AuxiliarLogica(operador,esLogico, auxiliar)
            else:
                
                self.reportarError("No hay una expresion logica valida ", self.tokenActual.fila, self.tokenActual.columna)                
                self.hacerBT(posicionInicial)
                return None
        else:
            self.hacerBT(posicionInicial)
            return None

            




    """
    <Decision>::= <sentenciaif>[<sentenciaElse>]
    """
    def esDecision(self):
        # busca una sentencia If
        sentIf = self.esSentenciaIf()
        # la sentencia if no puede ser None
        if sentIf != None:
            #busca sentencia Else no importa si es None o no 
            sentElse = self.esSentenciaElse()
            
            return Decision (sentIf, sentElse)
        return None

    """
    <SentenciaIf>::= if "(" <ExpresionLogica> ")" <BloqueSentencia>
    """
    def esSentenciaIf(self):
        # verifica que sea una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:
            # la palabra reservada debe de ser "if"
            if self.tokenActual.lexema == "if":
                self.obtenerSiguienteToken()
                # sigue un parentesis izquierdo
                if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:
                    self.obtenerSiguienteToken()
                    #busca una expresion logica
                    expresionLogica = self.esExpresionLogica()
                    # la expresion logica no puede ser None
                    if expresionLogica != None:
                        # sigue un parentesis derecho
                        if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                            self.obtenerSiguienteToken()
                            #busca que exista un bloque de sentencias
                            bloqueSentencias = self.esBloqueSentencias()
                            # verifica que el bloque de sentencias no sea None
                            if bloqueSentencias != None:
                                return SentIF (expresionLogica, bloqueSentencias)
                            else:
                                self.reportarError("Bloque de sentencias del if es invalido", self.tokenActual.fila, self.tokenActual.columna)
                        else:
                            self.reportarError("falta parentesis derecho", self.tokenActual.fila, self.tokenActual.columna)
                    else:
                        self.reportarError("falta expresion logica valida en el if", self.tokenActual.fila, self.tokenActual.columna)
                else:
                    self.reportarError("falta parentesis izquierdo", self.tokenActual.fila, self.tokenActual.columna)

        return None

    """
    <SentenciaElse>::= else <BloqueSentencia>
    """
    def esSentenciaElse(self):
        # verifica que sea una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:
            # la palabra reservada debe de ser "else"
            if self.tokenActual.lexema == "else":
                self.obtenerSiguienteToken()
                #busca que exista un bloque de sentencias
                bloqueSentencias = self.esBloqueSentencias()
                # verifica que el bloque de sentencias no sea None
                if bloqueSentencias != None:
                    return SentELSE (bloqueSentencias)
                else:
                    self.reportarError("Bloque de sentencias del else es invalido", self.tokenActual.fila, self.tokenActual.columna)
        return None

    """
    <DeclaracionVariable>::= <tipoDato> identificador [ "=" <lectura> | "=" <invocacion> |  "=" <Expresion> ] ";"
    """
    def esDeclaracionVariable(self):
        #comienza con una palabra reservada
        
        tipoDato = self.esTipoDato()
        if tipoDato != None:
            # la palabra reservada debe de ser un tipo de Dato            
            
            #Sigue un identificadoresTipoDat
            if self.tokenActual.categoria == Categoria.Identificador:
                identificador = self.tokenActual
                self.obtenerSiguienteToken()
                #sigue opcionalmente un "="
                lectura = None
                invocar = None
                expresion = None
                if self.tokenActual.lexema == "=":
                    self.obtenerSiguienteToken()
                    # obligatoriamente despues del igual debe de seguir una expresion
                    
                    #busca si es una lectura    
                    lectura = self.esLeer()
                    
                    #busca si es una invocacion
                    invocar = self.esInvocarMetodo()

                    #busca si es una expresion
                    expresion = self.esExpresion()

                    # si no es lectura, ni invocacion, ni expresion es un error sintactico 
                    if expresion == None and lectura == None and invocar == None:
                        self.reportarError("La asignacion de declaracion variable es invalida", self.tokenActual.fila, self.tokenActual.columna)
                    # la declaracion de variable finaliza con un fin de sentencia ";"
                    if self.tokenActual.categoria == Categoria.FinSentencia and expresion != None:
                        self.obtenerSiguienteToken()
                        return DeclaracionVariable(tipoDato, identificador, lectura, invocar, expresion)
                    elif lectura != None or invocar != None:
                        return DeclaracionVariable(tipoDato, identificador, lectura, invocar, expresion)
                else:
                    if self.tokenActual.categoria == Categoria.FinSentencia:
                        self.obtenerSiguienteToken()
                        return DeclaracionVariable(tipoDato, identificador, None, None, None)
            else:
                self.reportarError("No se encontro un identificador valido para la declaracion de una variable", self.tokenActual.fila, self.tokenActual.columna)
        
        return None        

    """
    <AsignacionVariable>::= identificador operadorAsignacion <expresion> ";" | identificador operadorAsignacion <Lectura> ";" | identificador operadorAsignacion <invocacion> ";"
    """
    def esAsignacionVariable(self):
        
        # obligatoriamente debe de iniciar con un identificador la asignacion de una variable
        if self.tokenActual.categoria == Categoria.Identificador:
            identificador = self.tokenActual
            self.obtenerSiguienteToken()

            # sigue obligatoriamente un operador de asignacion
            if self.tokenActual.categoria == Categoria.OperadorAsignacion:

                operadorAsignacion = self.tokenActual
                self.obtenerSiguienteToken()

                
                #busca si es una expresion
                expresion = self.esExpresion()

                #busca si es una lectura    
                lectura = self.esLeer()
                
                #busca si es una invocacion
                invocar = self.esInvocarMetodo()


                # si no es lectura, ni invocacion, ni expresion es un error sintactico 
                if expresion == None and lectura == None and invocar == None:
                    self.reportarError("La asignacion variable es invalida", self.tokenActual.fila, self.tokenActual.columna)
                
                # la declaracion de variable finaliza con un fin de sentencia ";"
                if self.tokenActual.categoria == Categoria.FinSentencia and expresion != None and lectura == None and invocar == None:
                    self.obtenerSiguienteToken()
                    return Asignacion(identificador, operadorAsignacion, None, None, expresion)
                elif lectura != None or invocar != None:
                    if lectura != None and invocar == None:
                        return Asignacion(identificador, operadorAsignacion, lectura, None, None)
                    elif lectura == None and invocar != None:
                        return Asignacion(identificador, operadorAsignacion, None, invocar, None)
                    else:
                        self.reportarError("solo puede ser una expreion, una lectura o una invacacion, no pueden ser varias al tiempo", self.tokenActual.fila, self.tokenActual.columna)
            else:
                self.reportarError("falta el operador de asignacion", self.tokenActual.fila, self.tokenActual.columna)

        return None

    """
    <Imprimir>::= imprimir "(" [<expresion>] ")" ";"
    """
    def esImprimir(self):

        # se debe de iniciar con una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:

            # la palabra reservada debe de ser "imprimir"
            if self.tokenActual.lexema == "imprimir":
                self.obtenerSiguienteToken()

                # verifica que siga un parentesis izquierdo
                if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:
                    self.obtenerSiguienteToken()

                    # busca si existe una expresion puede retornar None
                    expresion = self.esExpresion()

                    # se verifica que siga un parentesis derecho
                    if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                        self.obtenerSiguienteToken()

                        # la sentencia es imprimir termina con un fin de sentencia
                        if self.tokenActual.categoria == Categoria.FinSentencia:
                            self.obtenerSiguienteToken()

                            return Imprimir (expresion)

                        else:
                            self.reportarError("falta un final de sentencia \";\" en la sentencia imprimir", self.tokenActual.fila, self.tokenActual.columna)

                    else:
                        self.reportarError("falta el parentesis derecho en la sentencia imprimir", self.tokenActual.fila, self.tokenActual.columna)

                else:
                    self.reportarError("falta el parentesis izquierdo en la sentencia imprimir", self.tokenActual.fila, self.tokenActual.columna)

        return None

    """
    <Leer>::= leer "(" [<expresion>] ")" ";"
    """
    def esLeer(self):
        # se debe de iniciar con una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:

            # la palabra reservada debe de ser "leer""
            if self.tokenActual.lexema == "leer":
                self.obtenerSiguienteToken()

                # verifica que siga un parentesis izquierdo
                if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:
                    self.obtenerSiguienteToken()

                    # busca si existe una expresion puede retornar None
                    expresion = self.esExpresion()

                    # se verifica que siga un parentesis derecho
                    if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                        self.obtenerSiguienteToken()

                        # la sentencia es leer termina con un fin de sentencia
                        if self.tokenActual.categoria == Categoria.FinSentencia:
                            self.obtenerSiguienteToken()

                            return Leer (expresion)

                        else:
                            self.reportarError("falta un final de sentencia \";\" en la sentencia leer", self.tokenActual.fila, self.tokenActual.columna)

                    else:
                        self.reportarError("falta el parentesis derecho en la sentencia leer", self.tokenActual.fila, self.tokenActual.columna)

                else:
                    self.reportarError("falta el parentesis izquierdo en la sentencia leer", self.tokenActual.fila, self.tokenActual.columna)

        return None


    """
        <IncrementoDecremento>::=  identificador ++ ";" |    identificador -- ";" 
    """
    def esIncrementoDecremento(self):
        if self.tokenActual.categoria == Categoria.Identificador:
            identificador = self.tokenActual
            posInicio = self.posActual
            self.obtenerSiguienteToken()
            if self.tokenActual.categoria == Categoria.OperadorIncrementoDecremento:
                operador = self.tokenActual
                self.obtenerSiguienteToken()
                 #Verifica que la sentencia retorno termine con un fin de sentencia
                if self.tokenActual.categoria == Categoria.FinSentencia:
                    self.obtenerSiguienteToken()
                    return IncrementoDecremento(identificador,operador)
                else:
                    self.reportarError("El retorno no termino con \";\"", self.tokenActual.fila, self.tokenActual.columna)
            else:
                self.hacerBT(posInicio)
        
        return None



    """
    <Ciclo>::= while "(" <expresionLogica> ")" <bloqueSentencia>
    """
    def esCiclo(self):

        # se debe de iniciar con una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:

            # la palabra reservada debe de ser "while"
            if self.tokenActual.lexema == "while":
                self.obtenerSiguienteToken()

                # verifica que siga un parentesis izquierdo
                if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:
                    self.obtenerSiguienteToken()

                    # busca si existe una expresion logica 
                    expresionLogica = self.esExpresionLogica()

                    # la expresion logica no puede ser None
                    if expresionLogica != None:

                        # se verifica que siga un parentesis derecho
                        if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                            self.obtenerSiguienteToken()

                            # se busca un bloque de sentencias
                            bloqueSentencia = self.esBloqueSentencias()

                            # el bloque de sentencia no puede ser None
                            if bloqueSentencia != None:

                                return SentenceWhile (expresionLogica, bloqueSentencia)
                            
                            else:
                                self.reportarError("falta un bloque de sentencias para el ciclo", self.tokenActual.fila, self.tokenActual.columna)    
                        else:
                            self.reportarError("falta el parentesis derecho", self.tokenActual.fila, self.tokenActual.columna)
                    else:
                        self.reportarError("la expresion logica del ciclo es invalida", self.tokenActual.fila, self.tokenActual.columna)
                else:
                    self.reportarError("falta el parentesis izquierdo", self.tokenActual.fila, self.tokenActual.columna)

        return None

    """
    <Retorno>::= return <Expresion> ";" 
    """
    def esRetorno(self):

        #Verifica que sea una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:

            #Verifica que la palabra reservada sea return
            if self.tokenActual.lexema == "return":
                self.obtenerSiguienteToken()
                

                #Busca la expresion
                expresion = self.esExpresion()
                #Verifica que la expresion no sea nula
                if expresion != None:

                    #Verifica que la sentencia retorno termine con un fin de sentencia
                    if self.tokenActual.categoria == Categoria.FinSentencia:
                        self.obtenerSiguienteToken()

                        return Retorno(expresion)
                    else:
                        self.reportarError("El retorno no termino con \";\"", self.tokenActual.fila, self.tokenActual.columna)
                else:
                    self.reportarError("No hay una expresion valida de retorno", self.tokenActual.fila, self.tokenActual.columna)

        return None#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <InvocarMetodo>::= invocar identificador "(" [<ListaArgumentos>] ")" ";"
    """
    def esInvocarMetodo(self):

        # verifica que empiece con una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:

            # verifica que la palabra reservada sea "invocar"
            if self.tokenActual.lexema == "invocar":
                self.obtenerSiguienteToken()

                # debe de seguir un identificador y lo debe de guardar
                if self.tokenActual.categoria == Categoria.Identificador:

                    identificador = self.tokenActual
                    self.obtenerSiguienteToken()

                    # debe de seguir un parentesis Izquierdo
                    if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:
                        self.obtenerSiguienteToken()

                        #busca la lista de los argumentos
                        listaArgumentos = self.esListaArgumentos()

                        # la lista de argumentos no puede ser None
                        

                        # verifica que sigua un parentesis Derecho
                        if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                            self.obtenerSiguienteToken()

                            # verifica que la invocacion de una funcion termine con un fin de sentencia
                            if self.tokenActual.categoria == Categoria.FinSentencia:
                                self.obtenerSiguienteToken()

                                return InvocarFuncion(identificador, listaArgumentos)

                            else:
                                self.reportarError("falta finalizar la sentencia con \";\"", self.tokenActual.fila, self.tokenActual.columna)

                        else:
                            self.reportarError("falta parentesis derecho en invocar metodo", self.tokenActual.fila, self.tokenActual.columna)

                    else:
                        self.reportarError("falta parentesis izquierdo en invocar metodo", self.tokenActual.fila, self.tokenActual.columna)

                else:
                    self.reportarError("Identificador no encontrado en invocar metodo", self.tokenActual.fila, self.tokenActual.columna)

        return None

    """
    <ListaArgumentos>::= <Argumento> ["," <ListaArgumentos>]
    """
    def esListaArgumentos(self):

        # Se inicializa la lista de argumentos
        listaArgumentos = []

        # obligatoriamente debe de existir un argumento
        argumento = self.esArgumento()

        while argumento != None:

                # se agrega argumento actual
                listaArgumentos.append(argumento)

                # despues de ser agregado a la lista se vuelve nulo para hallar uno nuevo
                argumento = None
                
                # se pregunta si sigue un separador para agregar un nuevo argumento
                if self.tokenActual.categoria == Categoria.Separador:
                    self.obtenerSiguienteToken()

                    # se busca un nuevo argumento
                    argumento = self.esArgumento()

                    # el argumento no puede se None
                    if argumento == None:
                        self.reportarError("despues de la coma no se encontro un argumento valido", self.tokenActual.fila, self.tokenActual.columna)

        # se retorna la lista de argumentos del mapa
        return listaArgumentos

    """
    <Argumento>::= identificador | <expresion>
    """
    def esArgumento(self):

        # se verifica que sea un identificador
        expresion = self.esExpresion()
        if expresion !=None:
            # busca que sea una expresion
            # verifica que la expresion no sea nula
            
            return Argument(None, expresion) 
        # si no es un identificador
        elif self.tokenActual.categoria == Categoria.Identificador:
            
            identificador = self.tokenActual
            self.obtenerSiguienteToken()

            # guarda el identificador como un argumento
            return Argument(identificador, None)
           
        return None
    
    """
    <Arreglo>::= array <tipoDato> identificador "=" "[" <listaExpresiones> "]" ";"
    """
    def esArreglo(self):

        # se debe de empezar con una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:

            # la palabra reservarda es "array"
            if self.tokenActual.lexema == 'array':
                self.obtenerSiguienteToken()

                # se busca el tipo de dato del arreglo
                tipoDato = self.esTipoDato()
                # se verifica que el tipo de dato no sea None
                if tipoDato != None:

                    # despues, obligatoriamente debe de ir un identificador
                    if self.tokenActual.categoria == Categoria.Identificador:

                        # se guarda el identificador
                        identificador = self.tokenActual
                        self.obtenerSiguienteToken()

                        # se continua obligatoriamente con un "="
                        if self.tokenActual.lexema == "=":
                            self.obtenerSiguienteToken()

                            # sigue un corchete Izquierdo
                            if self.tokenActual.categoria == Categoria.CorcheteIzquierdo:
                                self.obtenerSiguienteToken()

                                # se busca la lista de expresiones
                                listaExpresiones = self.esListaExpresiones()
                                
                                # se verifica que la lista no llegue None
                                if listaExpresiones != None:

                                    # obligatoriamente debe de seguir un corcheteDerecho
                                    if self.tokenActual.categoria == Categoria.CorcheteDerecho:
                                        self.obtenerSiguienteToken()

                                        # por ultimo y no menos importante <3 se verifica que termine con un fin de sentencia
                                        if self.tokenActual.categoria == Categoria.FinSentencia:
                                            self.obtenerSiguienteToken()

                                            # se guarda el arreglo
                                            return Array (tipoDato, identificador, listaExpresiones)

                                        else:
                                            self.reportarError("la sentencia arreglo no finalizo con un \";\"", self.tokenActual.fila, self.tokenActual.columna)
                                    else:
                                        self.reportarError("falta corchete derecho \"]\"", self.tokenActual.fila, self.tokenActual.columna)
                                else:
                                    self.reportarError("la sentencia arreglo no finalizo con unno encontro una lista de expresiones valida", self.tokenActual.fila, self.tokenActual.columna)
                            else:
                                self.reportarError("falta corchete izquierdo \"[\"", self.tokenActual.fila, self.tokenActual.columna)
                        else:
                            self.reportarError("falta el operador de asignacion \"=\"", self.tokenActual.fila, self.tokenActual.columna)
                    else:
                        self.reportarError("no encuentra un identificador valido", self.tokenActual.fila, self.tokenActual.columna)
                else:
                    self.reportarError("tipo de dato invalido", self.tokenActual.fila, self.tokenActual.columna)
            
        return None 
    
    """
    <listaExpresiones>::= <Expresion> ["," <listaExpresiones> ]
    """
    def esListaExpresiones(self):

        # Se inicializa la lista de expresiones
        listaExpresiones = []

        # obligatoriamente debe de existir una expresion
        expresion = self.esExpresion()

        while expresion != None:

                # se agrega expresion actual
                listaExpresiones.append(expresion)

                # despues de ser agregada a la lista se vuelve nula para hallar una nueva
                expresion = None
                
                # se pregunta si sigue un separador para agregar una nueva expresion
                if self.tokenActual.categoria == Categoria.Separador:
                    self.obtenerSiguienteToken()

                    # se busca una nueva expresion
                    expresion = self.esExpresion()

                    # la expresion no puede se None
                    if expresion == None:
                        self.reportarError("despues de la coma no se encontro componente valido en el mapa", self.tokenActual.fila, self.tokenActual.columna)

        # se retorna la lista de expresions del mapa
        return listaExpresiones

    """
    <Mapa>::= map identificador "=" <listaComponentesMap>
    """
    def esMapa(self):

        # obligatoriamente se empieza con una palabra reservada
        if self.tokenActual.categoria == Categoria.PalabraReservada:
        
            # la palabra reservada debe de ser "map"
            if self.tokenActual.lexema == "map":
                self.obtenerSiguienteToken()

                # obligatoriamente debe de ir un identificador y se almacena
                if self.tokenActual.categoria == Categoria.Identificador:
                    identificador = self.tokenActual
                    self.obtenerSiguienteToken()

                    #obligatoriamente debe de ir un "="
                    if self.tokenActual.lexema == "=":
                        self.obtenerSiguienteToken()
                        
                        # se busca una lista de componentes del mapa
                        listaComponentes = self.esListaComponentesMapa()

                        # la lista no puede ser NONE
                        if listaComponentes != None:

                            # se retorna el mapa con la lista de componentes y el identiicador
                            return mapita (identificador, listaComponentes)

                        else:
                            self.reportarError("no existe lista de componentes del mapa",self.tokenActual.fila, self.tokenActual.columna)
                    else:
                        self.reportarError("falta el \"=\" en el mapa", self.tokenActual.fila, self.tokenActual.columna)
                else:        
                    self.reportarError("el mapa no tiene identificador",self.tokenActual.fila,self.tokenActual.columna)
        return None

    """
    <listaComponentesMap>::= "[" <componenteMap> [ "," <listaComponentesMap>] "]" ";"
    """
    def esListaComponentesMapa(self):

        if self.tokenActual.categoria == Categoria.CorcheteIzquierdo:
            # Se inicializa la lista de componentes del mapa
            self.obtenerSiguienteToken()

            listaComponentes = []

            # obligatoriamente debe de existir un componente del mapa
            componente = self.esComponenteMapa()

            # si componente retorna diferente de NONE sigue realiza el ciclo
            while componente != None:

                # se agrega componente actual
                listaComponentes.append(componente)

                # despues de ser agregada a la lista se vuelve nula para hallar una nueva
                componente = None
                
                # se pregunta si sigue un separador para agregar un nuevo componente
                if self.tokenActual.categoria == Categoria.Separador:
                    self.obtenerSiguienteToken()

                    # se busca un nuevo componente
                    componente = self.esComponenteMapa()

                    # el componente no puede se None
                    if componente == None:
                        self.reportarError("despues de la coma no se encontro componente valido en el mapa", self.tokenActual.fila, self.tokenActual.columna)

            # se verifica que efectivamente en la lista de componetentes exista al menos un componente
            if(len(listaComponentes) >= 1):
                
                # obligatoriamente debe de seguir un corchete Derecho
                if self.tokenActual.categoria == Categoria.CorcheteDerecho:
                    self.obtenerSiguienteToken()

                    # obligatoriamente debe de seguir un fin de sentencia
                    if self.tokenActual.categoria == Categoria.FinSentencia:
                        self.obtenerSiguienteToken()

                        # se retorna la lista de componentes del mapa
                        return listaComponentes
                    
                    else:
                        self.reportarError("Falta el final de sentencia \";\" de la sentencia map", self.tokenActual.fila, self.tokenActual.columna)
                else:
                    self.reportarError("Falta el corchete Derecho \"]\" en la sentencia map", self.tokenActual.fila, self.tokenActual.columna)
            else:
                self.reportarError("Falta almenos un componente el la lista de componentes del map", self.tokenActual.fila, self.tokenActual.columna)
            
            return None

    """
    <componenteMap>::= "(" <termino> "," <termino> ")"
    """
    def esComponenteMapa(self):
        # corchete izquierdo es obligatorio (no se guarda)
        if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:
            self.obtenerSiguienteToken()
            
            terminoLlave = self.esTermino()

            # termino llave es obligatorio 
            if terminoLlave != None:

                # separador es obligatorio (no se guarda)
                if self.tokenActual.categoria == Categoria.Separador:
                    self.obtenerSiguienteToken()

                    terminoClave = self.esTermino()

                    # termino clave es obligatorio
                    if terminoClave != None:

                        # corchete derecho es obligatorio (no se guarda)
                        if self.tokenActual.categoria == Categoria.ParentesisDerecho:
                            self.obtenerSiguienteToken()

                            return componenteMap (terminoLlave, terminoClave)
                                                        
                        else:
                            self.reportarError("Falta corchete derecho", self.tokenActual.fila, self.tokenActual.columna)
                            return None
                    else:
                        self.reportarError("Falta termino clave", self.tokenActual.fila, self.tokenActual.columna)
                        return None
            
                else:
                    self.reportarError("Falta separador", self.tokenActual.fila, self.tokenActual.columna)
                    return None
            else:
                self.reportarError("Falta termino llave", self.tokenActual.fila, self.tokenActual.columna)
                return None
        else:
            self.reportarError("Falta corchete derecho", self.tokenActual.fila, self.tokenActual.columna)   
        
        return None

    def getListaErrores(self):
        return self.listaErrores