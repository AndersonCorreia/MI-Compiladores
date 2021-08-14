from estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface

class TokenVazioState(EstadoAbertoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        return TokenVazioState
        
    @staticmethod
    def caractereCompoemLexema():
        return True