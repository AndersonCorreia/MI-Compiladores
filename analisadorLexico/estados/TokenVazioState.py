from analisadorLexico.estados.CaractereInvalidoState import CaractereInvalidoState
from analisadorLexico.estados.DelimitadorState import DelimitadorState
from analisadorLexico.estados.OperadorLogicoIncompletoState import OperadorLogicoIncompletoState
from analisadorLexico.estados.IndentificadorIncompletoState import IndentificadorIncompletoState
from analisadorLexico.estados.IndentificadorOuPalavraReservadaState import IndentificadorOuPalavraReservadaState
from estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class TokenVazioState(EstadoAbertoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        if isSimboloPermitido(char):
            if isLetra(char):
                if maybePalavraReservada(lexema):
                    return IndentificadorOuPalavraReservadaState
                return IndentificadorIncompletoState
            
            if maybeOperadorLogico(char):
                return OperadorLogicoIncompletoState
            
            if isDelimitador(char):
                if isDelimitadorSemToken(char):
                    return TokenVazioState
                return DelimitadorState
            
        return CaractereInvalidoState
        
    @staticmethod
    def caractereCompoemLexema():
        return False
    
    @staticmethod
    def finalDoArquivo( lexema ):
        return TokenVazioState