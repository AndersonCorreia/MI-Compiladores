from analisadorLexico.estados.AguardandoDelimitadorState import AguardandoDelimitadorState
from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class IndentificadorCompletoState(EstadoCompletoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        return AguardandoDelimitadorState
        
    @staticmethod
    def caractereCompoemLexema():
        return False
    
    @staticmethod
    def getTipo():
        return "identificador"
    
    @staticmethod
    def finalDoArquivo():
        return IndentificadorCompletoState