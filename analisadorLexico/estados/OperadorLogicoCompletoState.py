from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from analisadorLexico.estados.CaractereInvalidoState import CaractereInvalidoState
from estruturaLexica import *

class OperadorLogicoCompletoState(EstadoCompletoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        if isSimboloPermitido(char):
            return AguardandoDelimitadorState
            
        return CaractereInvalidoState
        
    @staticmethod
    def caractereCompoemLexema():
        return False
    
    @staticmethod
    def getTipo():
        return "operador logico"
    
    @staticmethod
    def finalDoArquivo( lexema ):
        return TokenVazioState