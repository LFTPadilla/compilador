# -.- encoding:UTF8 -*-
from AnalizadorLexico import Analizador

codigo = "identificador == 123 444.43"

analisisLexico = Analizador(codigo)

analisisLexico.analizar()
print ("hola")

print (analisisLexico.tokens)

