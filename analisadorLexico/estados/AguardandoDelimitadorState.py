from analisadorLexico.estados.AusenciaDeDelimitadorState import AusenciaDeDelimitadorState
from analisadorLexico.estados.DelimitadorState import DelimitadorState
from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from analisadorLexico.estados.TokenVazioState import TokenVazioState
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
    def finalDoArquivo( lexema ):
        return TokenVazioState