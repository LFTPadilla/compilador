from PyQt5 import QtWidgets

"""
    <SentenciaIf>::= if "(" <ExpresionLogica> ")" <BloqueSentencia>
"""
class SentIF:

    def __init__(self, expresionLogica, bloqueSentencias):
        self.expresionLogica = expresionLogica
        self.bloqueSentencias = bloqueSentencias


    def __repr__(self):
        return "(Sentencia If : ExpresionLogica: %s, bloqueSentencias: %s)" % (self.expresionLogica, self.bloqueSentencias)

    def __str__(self):
        return "Sentencia If [%s, %s]"% (self.expresionLogica, self.bloqueSentencias)
                
    def construirArbol(self, arbol):
        arbolIf = QtWidgets.QTreeWidgetItem(arbol)
        titulo = "If"
        arbolIf.setText(0,titulo)
        
        ramaExpresionLogica = QtWidgets.QTreeWidgetItem(arbolIf)
        ramaExpresionLogica.setText(0,"Expresion Logica")

        arbolExpresionLogica = QtWidgets.QTreeWidgetItem(ramaExpresionLogica)
        self.expresionLogica.construirArbol(arbolExpresionLogica)
        
        self.bloqueSentencias.construirArbol(arbolIf)

    def llenarTablaSimbolos(self,tablaSimbolos,erroresSemanticos):
        print("Sentencia IF")
        #Vamos a mandar como ambito "if" y la fila y columna en la que se encuentra
        self.bloqueSentencias.llenarTablaSimbolos(tablaSimbolos,erroresSemanticos,"if "+str(self.expresionLogica.expresionRelacional.operadorRelacional.fila)+","+str(self.expresionLogica.expresionRelacional.operadorRelacional.columna))
        
    def obtenerPythonCode(self):
        codigo = ""
        codigo = "if"
        codigo += "("+ self.expresionLogica.obtenerPythonCode() +")"
        codigo += self.bloqueSentencias.obtenerPythonCode()
        return codigo
        
    def analisisSemantico(self,tablaSimbolos,listaErrores):
        pass