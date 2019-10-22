
class errorSintactico:

    def __init__(self,msg,fil,col):
        self.mensaje =msg
        self.fila= fil
        self.col =col

    def __repr__(self):
        return "(ErrSint: msg: %s, fil:%s, col:%s)" % (self.mensaje,self.fila,self.col)

    def __str__(self):
        return "(ErrSint: msg: %s, fil:%s, col:%s)" % (self.mensaje,self.fila,self.col)
