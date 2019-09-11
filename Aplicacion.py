# -.- encoding:UTF8 -*-
from AnalizadorLexico import Analizador

codigo = "546 <= < > >= == = /*** jh/gyg8*7tu 423***42 12 smdn*asdf **/"

analisisLexico = Analizador(codigo)
print("2")
analisisLexico.analizar()
print("3")
print (analisisLexico.tokens)

