# -.- encoding:UTF8 -*-
from AnalizadorLexico import Analizador

codigo = "hola as)(d _asd)f /*asdfsdFAS asdfsDF*/"

analisisLexico = Analizador(codigo)
print("2")
analisisLexico.analizar()
print("3")
print (analisisLexico.tokens)

