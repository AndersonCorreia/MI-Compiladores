from analisadorLexico.estados.AusenciaDeDelimitadorState import AusenciaDeDelimitadorState
from analisadorLexico.estados.DelimitadorState import DelimitadorState
from estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class AguardandoDelimitadorState(EstadoAbertoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        if isDelimitador(char):
            if isDelimitadorSemToken(char):
                return TokenVazioState
            
            return DelimitadorState
        
        return AusenciaDeDelimitadorState
        
    @staticmethod
    def caractereCompoemLexema():
        return False
    
    @staticmethod
    def finalDoArquivo():
        return TokenVazioState