import abc
from abc import ABCMeta

class Expression:
    
    __metaclass__ = ABCMeta

    def __init_(self):
        pass
        
    @abc.abstractamethod
    def getArbolVisual(self):
        pass