# -.- encoding:UTF8 -*-
from logica.lexico.AnalizadorLexico import Analizador

codigo = "hola for as)(d _asd)f \"asdfsdFAS asdfsD"

analisisLexico = Analizador(codigo)
print("2")
analisisLexico.analizar()
print("3")
print (analisisLexico.tokens)

