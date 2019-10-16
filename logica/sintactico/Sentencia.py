import abc
from abc import ABCMeta

class Sentence(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abc.abstractamethod
    def getArbolVisual(self):
        