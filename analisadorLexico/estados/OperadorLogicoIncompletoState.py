from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class OperadorLogicoIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isDelimitador(char):
                if isOperadorLogico(lexema):
                    return self.automato.setEstado("OperadorLogicoCompleto")
                return self.automato.setEstado("CaractereInvalido") # depois trocar para o estado de simbolo
            
            if ( maybeOperadorLogico(lexema) ):
                return self.automato.setEstado("OperadorLogicoIncompleto")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isOperadorLogico(lexema):
            return self.automato.setEstado("OperadorLogicoCompleto")
        return self.automato.setEstado("CaractereInvalido") # depois trocar para o estado de simbolo