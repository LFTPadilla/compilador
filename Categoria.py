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
    Llaves = 9
    Parentesis = 10
    Corchetes = 11
    FinSentencia = 12
    Separador = 13
    PuntoDosPuntos = 14
    ComentarioLinea = 15
    ComentarioBloque = 16
    CadenaCaracteres = 17
    Caracter = 18
    Desconocido = 19