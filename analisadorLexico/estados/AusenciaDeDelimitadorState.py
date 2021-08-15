from estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *

class AusenciaDeDelimitadorState(EstadoDeErrorInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        return AusenciaDeDelimitadorState
        
    @staticmethod
    def caractereCompoemLexema():
        return True
    
    @staticmethod
    def finalDoArquivo():
        return TokenVazioState