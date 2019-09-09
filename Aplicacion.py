# -.- encoding:UTF8 -*-
from AnalizadorLexico import Analizador

codigo = "546 /*** jh/gyg8*7tu 423***42 12 smdn*asdf **/"

analisisLexico = Analizador(codigo)

analisisLexico.analizar()

print (analisisLexico.tokens)

