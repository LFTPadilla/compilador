# -.- encoding:UTF8 -*-
from AnalizadorLexico import Analizador

codigo = "== 123 !=444.43"
print("1")
analisisLexico = Analizador(codigo)
print("2")
analisisLexico.analizar()
print("f")
print (analisisLexico.tokens)

