

class UnidadDeCompilacion:

    def __init__(self, listaFunciones):
        self.listaFunciones = listaFunciones

    def getArbolVisual(self):
        DefaultMutabletreeNode raiz = new DefaultMutabletreeNode("unidad de compilacion")
        raiz.add( new DefaultMutabletreeNode("hijo 1"))
        return raiz;
        