from estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class DelimitadorState(EstadoCompletoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        return TokenVazioState
        
    @staticmethod
    def caractereCompoemLexema():
        return True
    
    @staticmethod
    def getTipo():
        return "delimitador"
    
    @staticmethod
    def finalDoArquivo():
        return TokenVazioState