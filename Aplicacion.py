# -.- encoding:UTF8 -*-
from AnalizadorLexico import Analizador

codigo = "hola asd _asdf /*asdfsdFAS asdfsDF*/"

analisisLexico = Analizador(codigo)
print("2")
analisisLexico.analizar()
print("3")
print (analisisLexico.tokens)

