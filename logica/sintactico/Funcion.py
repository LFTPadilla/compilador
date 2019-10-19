from PyQt5 import QtWidgets


class Function:

    def __init__(self, visibilidad, retorno, identificador, parametros, bloque):
        self.visibilidad = visibilidad
        self.identificador = identificador
        self.parametros = parametros
        self.retorno = retorno
        self.bloque = bloque

    def construirArbol(self, arbol, n):
        arbolFuncion = QtWidgets.QTreeWidgetItem(arbol)

        titulo = "Funcion "+str(n)
        arbolFuncion.setText(0,titulo)

        visi = QtWidgets.QTreeWidgetItem(arbolFuncion)
        visi.setText(0,"Visibilidad "+self.visibilidad.lexema)
        
        
        retor = QtWidgets.QTreeWidgetItem(arbolFuncion)
        retor.setText(0,"Retorno "+self.retorno.lexema)
        
        ident = QtWidgets.QTreeWidgetItem(arbolFuncion)
        ident.setText(0,"Nombre "+self.identificador.lexema)


        bloq = QtWidgets.QTreeWidgetItem(arbolFuncion)
        bloq.setText(0,"Bloque Sentecias")

        #AQUI FOR QUE RECORRA LAS SENTENCIAS

        param = QtWidgets.QTreeWidgetItem(arbolFuncion)
        param.setText(0,"Parametros")
        cont=0
        for parametro in self.parametros:
            par = QtWidgets.QTreeWidgetItem(param)
            par.setText(0,"Parametro "+str(cont))
            cont+=1

            i = QtWidgets.QTreeWidgetItem(par)
            i.setText(0,parametro.identificador.lexema)

            tip = QtWidgets.QTreeWidgetItem(par)
            tip.setText(0,parametro.tipoRetorno.lexema)
            #p = str(parametro.tipoRetorno.lexema)+" "+str(parametro.identificador.lexema)
            
        
        

    def __repr__(self):
        return "(Funcion: visibilidad: %s, identificador: %s, parametros: %s, retorno: %s, bloqueSentencias: %s)" % (self.visibilidad, self.identificador, self.parametros, self.retorno, self.bloque)

    def __str__(self):
        return "Funcion [%s, %s, %s, %s, %s]"% (self.visibilidad, self.identificador, self.parametros, self.retorno, self.bloque)