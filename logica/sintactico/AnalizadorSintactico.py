
from logica.lexico.Token import Token
from logica.lexico.Categoria import Categoria

from PyQt5 import QtWidgets

from logica.sintactico.UnidadCompilacion import UnidadComp

from logica.sintactico.Funcion import Function
from logica.sintactico.Error import errorSintactico

from logica.sintactico.Parametro import Parameter
from logica.sintactico.Argumento import Argument
from logica.sintactico.Arreglo import Array

from logica.sintactico.Sentencia import Sentence
from logica.sintactico.SentenciaAsignacion import Asignacion
from logica.sintactico.SentenciaDeclararVariable import DeclaracionVariable
from logica.sintactico.SentenciaIfElse import IfElse
from logica.sintactico.SentenciaImprimir import Imprimir
from logica.sintactico.SentenciaInvocarFuncion import InvocarFuncion
from logica.sintactico.SentenciaLeer import Leer
from logica.sintactico.SentenciaRetorno import Retorno
from logica.sintactico.SentenciaWhile import SentenceWhile

from logica.sintactico.Expresion import Expression
from logica.sintactico.ExpresionAritmetica import Aritmetica 
from logica.sintactico.ExpresionCadena import Cadena
from logica.sintactico.ExpresionLogica import Logica
from logica.sintactico.ExpresionRelacional import Relacional

from logica.sintactico.ExpresionAuxiliarAritmetica import AuxiliarAritmetica
from logica.sintactico.ExpresionAuxiliarRelacional import AuxiliarRelacional
from logica.sintactico.ExpresionAuxiliarLogica import AuxiliarLogica

from logica.sintactico.Mapa import mapita
from logica.sintactico.ComponenteMapa import componenteMap



class ASintactico: 
    arbol = None
    listaTokens = []
    posActual = 0
    listaErrores = []
    contFunciones = 0
    palabrasReservadas =[]

    def __init__(self,listaTokens,arbol):
        self.arbol = arbol
        self.listaTokens = listaTokens
        self.tokenActual = self.listaTokens[self.posActual]
        self.palabrasReservadas = ["String","abstract","continue","for","new","switch","assert","default","goto","package","synchronized","boolean","do","if","private","this","break","double","implements","protected","throw","byte","else","import","public","throws","case","enum","instanceof","return","transient","catch","extends","int","short","try","char","final","interface","static","void","class","finally","long","strictfp","volatile","const","float","native","super","while","map", "array"]

    def reportarError(self,msj,f,c):
        err = errorSintactico(msj,f,c)
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
            return UnidadComp(listaFunciones)
        
        return None
    
    """
        <ListaFunciones> ::= <Funcion>[<ListaFunciones>]
    """
    def esListaFunciones(self):           
        lista = []
        f = self.esFuncion()
        while f != None:
            lista.append(f)
            f = self.esFuncion()
        return lista

    """
       <Funcion> ::= [<visibilidad>] <TipoRetorno> Identificador "(" [<ListaParamentros>] ")" "{" <bloqueSentencias> "}"

    """
    def esFuncion(self):

        print("token ",self.tokenActual)
        #El token de visibilidad es opcional, por eso esta en un if que de no cumplirse, no pasa nada
        visibilidad  = self.esVisibilidad()
               
        #El tipo de retorno es obligatorio  
        tipoRetorno = self.esTipoRetorno()  
        if tipoRetorno!=None :
           
            #El identificador es obligatorio             
            if self.tokenActual.categoria == Categoria.Identificador:
                identificador = self.tokenActual
                print("El ident", identificador)
                self.obtenerSiguienteToken()
                print("parentesis izq",self.tokenActual)
                #El parentesis izquierdo es obligatorio pero no se guarda
                if self.tokenActual.categoria == Categoria.ParentesisIzquierdo:

                    self.obtenerSiguienteToken()
                    print("Paso a parametros",self.tokenActual)
                    #La lista de parametros no es obligatoria, solo se guarda de haber algo
                    parametros = self.esListaParametros()   
                    print("Lista parametros ",parametros)
                    #El parentesis derecho es obligario pero no se guarda
                    if(self.tokenActual.categoria == Categoria.ParentesisDerecho):

                        self.obtenerSiguienteToken()
                        print("bloque ",self.tokenActual)
                        #El bloque de sentencias se guarda 
                        bloque = self.esBloqueSentencias()#BloqueSentencia 
                        if(bloque != None ): #return cuenta como sentencia y minimo debe tenerlo 
                     
                            f = Function(visibilidad,tipoRetorno,identificador,parametros,bloque)
                            print("FUNCION ",f)
                            f.construirArbol(self.arbol,self.contFunciones)

                            print("Debe ser siguiente funcion ",self.tokenActual)
                            self.contFunciones+=1

                            return f
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
        return None

    """
    <Visibilidad> ::= public | private | protected | default
    """
    def esVisibilidad(self):
        if(self.tokenActual.categoria == Categoria.PalabraReservada):        
            if(self.tokenActual.lexema == "public" or self.tokenActual.lexema == "private" or self.tokenActual.lexema == "protected" or self.tokenActual.lexema == "default"):
                visi = self.tokenActual
                self.obtenerSiguienteToken()
                
                return visi
        return None

    """
    <TipoRetorno> ::= int | String | double | boolean | char | void
    """
    def esTipoRetorno(self):
        if self.tokenActual.categoria == Categoria.PalabraReservada:
            if self.tokenActual.lexema == "int" or self.tokenActual.lexema == "String" or self.tokenActual.lexema == "double" or self.tokenActual.lexema == "boolean" or self.tokenActual.lexema == "char" or self.tokenActual.lexema == "void":
                tipoRet = self.tokenActual
                print("Debe ser tipo ret ",tipoRet)
                self.obtenerSiguienteToken()
                print("Aqui identificador ",self.tokenActual)
                return tipoRet
        return None
    
    
    """
    <TipoDato> ::= int | String | double | boolean | char
    """
    def esTipoDato(self):
        if self.tokenActual.categoria == Categoria.PalabraReservada:
            if self.tokenActual.lexema == "int" or self.tokenActual.lexema == "String" or self.tokenActual.lexema == "double" or self.tokenActual.lexema == "boolean" or self.tokenActual.lexema == "char":
                tipoDato = self.tokenActual
                self.obtenerSiguienteToken()
                return tipoDato
        return False        
    
    """
    <ListaParametros> ::= <Parametro> [","<listaParametros>]
    """
    def esListaParametros(self):
        lista = []
        f = self.esParametro()
        while(f!=None):
            lista.append(f)
            f=None
            if(","): #falta la coma
                f = self.esParametro()
        return lista
        
    """
    <Parametro> ::= <TipoDato> identificador
    """   
    def esParametro(self):
        
        tipo_dato = self.esTipoDato()
        if ( not tipo_dato == False ):                                      #si el token actual es un tipo de dato
            if ( self.tokenActual.categoria == Categoria.Identificador ):   #
                
                nombre = self.tokenActual
                self.obtenerSiguienteToken()
                return Parameter(tipo_dato,nombre)
            else:
                self.reportarError("No hay identificador definido para el parametro", self.tokenActual.fila, self.tokenActual.columna)
        else:
            self.reportarError("No hay tipo de dato definido para el parametro", self.tokenActual.fila, self.tokenActual.columna)
    
    """
        <BloqueSentencia> ::= "{" [<listaSentencias>] "}"
    """
    def esBloqueSentencias(self):
        if(self.tokenActual.categoria == Categoria.LlaveIzquierda):
            self.obtenerSiguienteToken()
            print("Llego llave izq")
            sentencias = self.esListaSentencias()
            print("lista de sent ",sentencias)
            
            if(self.tokenActual.categoria == Categoria.LlaveDerecha):
                print("LLego llave der")
                self.obtenerSiguienteToken()
                return sentencias
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
        f = self.esSentencia()
        print("Sentencia ",f,self.tokenActual)
        while(f!=None):
            lista.append(f)
            f = self.esSentencia()
        print("SIGUIENTE FUNCION ",self.tokenActual)
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
        
        s = self.esImprimir()

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

        s = self.esMapa()

        if(s!=None):
            return s

        return s

    
    """
    <Expresion>::= <ExpresionAritmetica> | <ExpresionLogica> |<ExpresionRelacional> |<ExpresionCadena>
    """
    def esExpresion(self):
        
        e = None
        
        e = self.esExpresionAritmetica()
        
        if e != None:
            return e
        
        e = self.esExpresionRelacional()
        
        if e != None:
            return e
        
        e = self.esExpresionCadena()
        
        if e != None:
            return e
        
        #e = self.esExpresionLogica()
        
        if e != None:
            return e
             
        



    """
    <ExpresionAritmetica>::= "("<ExpresionAritmetica>")"[<ExpresionAuxiliar>] | <Termino>[<ExpresionAuxiliar>]
    """
    def esExpresionAritmetica(self):
        if self.tokenActual.categoria == Categoria.ParentesisIzquierdo or self.esTermino()!=None : 
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
                termino = self.esTermino()
                if(termino != None):
                    ea = self.esExpresionAuxiliarAritmetica()
                    return Aritmetica(None, ea , termino)
        return None

 
    """
    <ExpresionAuxiliar>::= operadorAritmetico <ExpresionAritmetica> [<ExpresionAuxiliar>]
    """
    def esExpresionAuxiliarAritmetica(self):
        if(self.tokenActual.categoria == Categoria.OperadorAritmetico):
            operador = self.tokenActual
            self.obtenerSiguienteToken()
            ea = self.esExpresionAritmetica()
            if(ea != None):
                eAux = self.esExpresionAritmetica()
                return AuxiliarAritmetica(operador,ea,eAux)                     
                

    """
    <ExpresionRelacional>::= "("<ExpresionRelacional>")"[<ExpresionAuxiliarRela>] | <Termino> [<ExpresionAuxiliarRela>]
    """
    def esExpresionRelacional(self):   
        if self.tokenActual.categoria == Categoria.ParentesisIzquierdo or self.esTermino != None : 
            if self.tokenActual.categoria == Categoria.ParentesisIzquierdo :
                self.obtenerSiguienteToken()
                er = self.esExpresionRelacional()
                if er != None :
                    self.obtenerSiguienteToken()
                    if self.tokenActual.categoria == Categoria.ParentesisDerecho :
                        self.obtenerSiguienteToken()
                        ear = self.esExpresionAuxiliarRelacional()
                        return Relacional(er,ear,None)
                    else:
                        self.reportarError("Falta parentesis derecho en la expresion relacional",self.tokenActual.fila, self.tokenActual.columna)
                        return None
                else:
                    self.reportarError("No hay una expresion relacional valida dentro de los parentesis",self.tokenActual.fila, self.tokenActual.columna)        
                    return None
            else:
                termino = self.esTermino()
                if termino != None: #si es un termino valido         
                    self.obtenerSiguienteToken()
                    ear = self.esExpresionAuxiliarRelacional()
                    return Relacional(None, ear,termino)
                #aca no se reporta el error de que "falta un termino valido" ya que si no hay parentesis izquierdo
                #  y tampoco hay un termino, ni siquiera seria una expresion  
        else: 
            return None                  
    
    """
    <ExpresionAuxiliarRelacional>::= operadorRelacional <ExpresionRelacional>[<ExpresionAuxiliarRelacional>]
    """
    def esExpresionAuxiliarRelacional(self):
        
        if self.tokenActual.categoria == Categoria.OperadorRelacional :
            opRelacional = self.tokenActual
            self.obtenerSiguienteToken()
            er = self.esExpresionRelacional()
            if er != None:
                self.obtenerSiguienteToken()
                ear = self.esExpresionAuxiliarRelacional()
                return AuxiliarRelacional(opRelacional,er,ear)
            else:
                self.reportarError("Falta una expresion relacional valida",self.tokenActual.fila,self.tokenActual.columna)
                return None
        else:
            self.reportarError("No hay un operador relacional",self.tokenActual.fila,self.tokenActual.columna)                
            return None
            
    
    
    """
    <Termino>::= <ValorNumerico> | identificador
    """    
    def esTermino(self):
        
        if(self.esValorNumerico() != None or self.tokenActual.categoria == Categoria.Identificador):
            return self.tokenActual
        return None

    """
    <ValorNumerico>::= numeroNatural | numeroReal    
    """
    def esValorNumerico(self):
        
        if(self.tokenActual.categoria == Categoria.NumeroNatural or self.tokenActual.categoria == Categoria.NumeroReal):
            return self.tokenActual
        return None

    """
    <ExpresionCadena>::= cadena "+" <Expresion> 
    
    """
    def esExpresionCadena(self):
        
        if self.tokenActual.categoria == Categoria.CadenaCaracteres :
            cadena = self.tokenActual
            self.obtenerSiguienteToken()
            if self.tokenActual.lexema == "+":
                
                self.obtenerSiguienteToken()
                e = self.esExpresion()
                return Cadena(cadena, e)
            else:
                self.reportarError("No hay '+' para concatenar", self.tokenActual.fila, self.tokenActual.columna)
        else:
            return None        
                
                
    
    """
    <ExpresionLogica>::= "!" <ExpresionLogica> [<ExpresionAuxiliarLogica>] | <ExpresionRelacional> [<ExpresionAuxiliarLogica>]
    """
    def esExpresionLogica(self):
        
        if self.tokenActual.lexema == '!' or self.esExpresionRelacional() :
            
            if self.tokenActual.lexema == '!' : 
                self.obtenerSiguienteToken()
                if self.esExpresionLogica():
                    e = self.tokenActual
                    self.obtenerSiguienteToken()
                    eal = self.esExpresionAuxiliarLogica()
                    
                    return Logica("!", e, eal, None)
                else:
                    self.reportarError("Expresion logica no valida",self.tokenActual.fila, self.tokenActual.columna)
            
            elif self.esExpresionRelacional():
                er = self.tokenActual
                self.obtenerSiguienteToken()
                eal = self.esExpresionAuxiliarLogica()
                return Logica(None, None, eal, er)                    
        else:
            return None    
        
    
    

    """
    <ExpresionAuxiliarLogica>::= operadorLogicoBinario <ExpresionLogica> [<ExpresionAuxiliarLogica>] 
    """
    def esExpresionAuxiliarLogica(self):
        
        if self.tokenActual.categoria == Categoria.OperadorLogico :
            
            self.obtenerSiguienteToken()
            
            if self.tokenActual.lexema == "&&" or self.tokenActual.lexema == "||" :
                opBin = self.tokenActual
                self.obtenerSiguienteToken()
                
                if self.esExpresionLogica():
                    e = self.tokenActual
                    self.obtenerSiguienteToken()
                    eal = self.esExpresionAuxiliarLogica()
        if self.tokenActual.categoria == Categoria.OperadorRelac
                    
                    return AuxiliarLogica(opBin, e, eal)
        else:
            return None    
        
    
            
    
    """
    <Decision>::= <sentenciaif>[<sentenciaElse>]
    """

    def esDecision(self):
        a = None
        return a

    """
    <SentenciaIf>::= if "(" <ExpresionLogica> ")" <BloqueSentencia>
    """
    def esSentenciaIf(self):
        a = None
        return a #se puso true, para que no arroje error su declaracionen el metodo esSentencia, es None

    """
    <SentenciaElse>::= else <BloqueSentencia>
    """
    def esSentenciaElse(self):
        a = None
        return a #se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <DeclaracionVariable>::= <tipoRetorno> identificador [ "=" <Expresion> ] ";"
    """
    def esDeclaracionVariable(self):
        a = None
        return a#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <AsignacionVariable>::= identificador operadorAsignacion <expresion> ";"
    """
    def esAsignacionVariable(self):
        a = None
        return a  #se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <Imprimir>::= imprimir "(" [<expresion>] ")" ";"
    """
    def esImprimir(self):
        a = None
        return a#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <Leer>::= leer "(" [<expresion>] ")" ";"
    """
    def esLeer(self):
        a = None
        return a#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <Ciclo>::= while "(" <expresionLogica> ")" <bloqueSentencia>
    """
    def esCiclo(self):
        a = None
        return a#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <Retorno>::= retorno <Expresion> ";"
    """
    def esRetorno(self):
        print("ENTRO A VERIFICAR RETORNO")
        if self.tokenActual.lexema == "return":
            self.obtenerSiguienteToken()
            e = self.esExpresion()
            print("Paso ES EXPRESION ",e)

            if e!=None:
                self.obtenerSiguienteToken()
                if self.tokenActual.categoria == Categoria.FinSentencia:
                    self.obtenerSiguienteToken()
                    print("Va a retornar el retorno ",self.tokenActual)
                    return Retorno(e)
            else:
                self.reportarError("No hay una expresion valida de retorno",self.tokenActual.fila,self.tokenActual.columna)

        return None#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <InvocarMetodo>::= invocar identificador "(" <ListaArgumentos> ")" ";"
    """
    def esInvocarMetodo(self):
        a = None
        return a#se puso true, para que no arroje error su declaracionen el metodo esSentencia

    """
    <ListaArgumentos>::= <Argumento> ["," <ListaArgumentos>]
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

        # se verifica que sea un identificador
        if self.tokenActual.categoria == Categoria.Identificador:
            identificador = self.tokenActual
            self.obtenerSiguienteToken()

            # guarda el identificador como un argumento
            return Argument(identificador, None)
            
        # si no es un identificador
        else:

            # busca que sea una expresion
            expresion = self.esExpresion()
            
            # verifica que la expresion no sea nula
            if expresion != None:
                
                # guarda la expresion como un argumento
                return Argument(None, expresion)
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
            else:
                self.reportarError("la palabra reservada no es \"array\"", self.tokenActual.fila, self.tokenActual.columna)
        else:
            self.reportarError("se debe de empezar con una palabra reservada", self.tokenActual.fila, self.tokenActual.columna)

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
            else:            
                self.reportarError("la palabra reservada no es la correcta para iniciar un mapa", self.tokenActual.fila, self.tokenActual.columna)
        else:
            self.reportarError("no es una palabra reservada", self.tokenActual.fila, self.tokenActual.columna)        
        return None

    """
    <listaComponentesMap>::= "[" <componenteMap> [ "," <listaComponentesMap>] "]" ";"
    """
    def esListaComponentesMapa(self):

        if self.tokenActual.categoria == Categoria.CorcheteIzquierdo:
            # Se inicializa la lista de componentes del mapa
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
                self.obtenerSiguienteToken()

                # separador es obligatorio (no se guarda)
                if self.tokenActual.categoria == Categoria.Separador:
                    self.obtenerSiguienteToken()

                    terminoClave = self.esTermino()

                    # termino clave es obligatorio
                    if terminoClave != None:
                        self.obtenerSiguienteToken()

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