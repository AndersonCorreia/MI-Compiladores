from analisadorLexico.estados.OperadorLogicoCompletoState import OperadorLogicoCompletoState
from analisadorLexico.estados.CaractereInvalidoState import CaractereInvalidoState
from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class OperadorLogicoIncompletoState(EstadoAbertoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        if isSimboloPermitido(char):
            if isDelimitador(char):
                if isOperadorLogico(lexema):
                    return OperadorLogicoCompletoState
                return CaractereInvalidoState # depois trocar para o estado de simbolo
            
            if ( maybeOperadorLogico(lexema) ):
                return OperadorLogicoIncompletoState
            
        return CaractereInvalidoState
        
    @staticmethod
    def caractereCompoemLexema():
        return True
    
    @staticmethod
    def finalDoArquivo( lexema ):
        if isOperadorLogico(lexema):
            return OperadorLogicoCompletoState
        return CaractereInvalidoState # depois trocar para o estado de simbolo