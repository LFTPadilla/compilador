from enum import Enum

class Categoria(Enum):
    Identificador = 1
    NumeroReal = 2
    NumeroNatural = 3
    OperadorAritmetico = 4
    OperadorAsignacion = 5
    OperadorIncrementoDecremento = 6
    OperadorRelacional = 7
    OperadorLogico = 8
    LlaveIzquierda = 9
    ParentesisDerecho = 10
    CorcheteIzquierdo = 11
    FinSentencia = 12
    Separador = 13
    Punto = 14
    ComentarioLinea = 15
    ComentarioBloque = 16
    CadenaCaracteres = 17
    Caracter = 18
    Desconocido = 19
    ErrorLexico = 20
    PalabraReservada =21
    ParentesisIzquierdo = 22
    DosPuntos = 23
    LlaveDerecha = 24
    CorcheteDerecho = 25