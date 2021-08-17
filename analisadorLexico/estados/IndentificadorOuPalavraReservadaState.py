from analisadorLexico.estados.CaractereInvalidoState import CaractereInvalidoState
from analisadorLexico.estados.IndentificadorCompletoState import IndentificadorCompletoState
from analisadorLexico.estados.IndentificadorIncompletoState import IndentificadorIncompletoState
from analisadorLexico.estados.PalavraReservadaState import PalavraReservadaState
from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class IndentificadorOuPalavraReservadaState(EstadoAbertoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        if isSimboloPermitido(char):
            if isLetraDigito(char) or char == '_':
                if maybePalavraReservada(lexema):
                    return IndentificadorOuPalavraReservadaState
                
                return IndentificadorIncompletoState
            
            if isDelimitador(char):
                if isPalavraReservada(lexema):
                    return PalavraReservadaState
                return IndentificadorCompletoState
            
        return CaractereInvalidoState
        
    @staticmethod
    def caractereCompoemLexema():
        return True
    
    @staticmethod
    def finalDoArquivo():
        return IndentificadorCompletoState