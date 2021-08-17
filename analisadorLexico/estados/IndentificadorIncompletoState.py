from analisadorLexico.estados import IndentificadorCompletoState
from analisadorLexico.estados.CaractereInvalidoState import CaractereInvalidoState
from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class IndentificadorIncompletoState(EstadoAbertoInterface):
    
    @staticmethod
    def getProximoEstado(char, lexema):
        if isSimboloPermitido(char):
            if isLetraDigito(char) or char == '_':
                return IndentificadorIncompletoState
            if isDelimitador(char):
                return IndentificadorCompletoState
            
        return CaractereInvalidoState
        
    @staticmethod
    def caractereCompoemLexema():
        return True
    
    @staticmethod
    def finalDoArquivo():
        return IndentificadorCompletoState