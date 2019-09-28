# -.- encoding:UTF8 -*-
from logica.lexico.AnalizadorLexico import Analizador
from logica.sintactico.AnalizadorSintactico import ASintactico

codigo = "  \" Hola \h jejje \"  "

analisisLexico = Analizador(codigo)
analisisLexico.analizar()

#aSintactico = ASintactico(analisisLexico.getListaTokens)

print (analisisLexico.tokens)

#print(aSintactico.esUnidadDeCompilacion())

#print(aSintactico.getListaErrores())



