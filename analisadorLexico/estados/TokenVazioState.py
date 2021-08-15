from analisadorLexico.estados.DelimitadorState import DelimitadorState
from analisadorLexico.estados.IndentificadorIncompletoState import IndentificadorIncompletoState
from analisadorLexico.estados.CaractereInvalidoState import CaractereInvalidoState
from analisadorLexico.estados.AguardandoDelimitadorState import AguardandoDelimitadorState
from estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class TokenVazioState(EstadoAbertoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        if isSimboloPermitido(char):
            if isLetra(char):
                return IndentificadorIncompletoState
            if isDelimitador(char):
                if isDelimitadorSemToken(char):
                    return TokenVazioState
                return DelimitadorState
            
        return CaractereInvalidoState
        
    @staticmethod
    def caractereCompoemLexema():
        return False
    
    @staticmethod
    def finalDoArquivo():
        return TokenVazioState