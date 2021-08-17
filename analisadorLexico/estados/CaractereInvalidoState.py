from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *

class CaractereInvalidoState(EstadoDeErrorInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        return CaractereInvalidoState
        
    @staticmethod
    def caractereCompoemLexema():
        return True
    
    @staticmethod
    def getTipo():
        return "simbolo invalido"
    
    @staticmethod
    def finalDoArquivo():
        return TokenVazioState