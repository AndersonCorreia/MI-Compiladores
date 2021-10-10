from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from analisadorLexico.estruturaLexica import *

class IndentificadorIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isLetraDigito(char) or char == '_':
                return self.automato.setEstado("IndentificadorIncompleto")
            if isDelimitador(char):
                return self.automato.setEstado("IndentificadorCompleto")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("IndentificadorCompleto")