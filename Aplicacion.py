# -.- encoding:UTF8 -*-
from AnalizadorLexico import Analizador

codigo = "15+++=+   ,//hola\n--"
print("1")
analisisLexico = Analizador(codigo)
print("2")
analisisLexico.analizar()
print("3")
print (analisisLexico.tokens)

