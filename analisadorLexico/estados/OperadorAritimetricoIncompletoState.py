from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class OperadorAritimetricoIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isDelimitador(char):
                if isOperadorAritimetrico(lexema):
                    return self.automato.setEstado("OperadorAritimetricoCompleto")
                return self.automato.setEstado("CaractereInvalido") # depois trocar para o estado de simbolo
            
            if ( maybeOperadorAritimetrico(lexema) ):
                return self.automato.setEstado("OperadorAritimetricoIncompleto")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isOperadorLogico(lexema):
            return self.automato.setEstado("OperadorAritimetricoCompleto")
        return self.automato.setEstado("CaractereInvalido") # depois trocar para o estado de simbolo