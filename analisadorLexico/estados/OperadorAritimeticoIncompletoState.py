from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class OperadorAritimeticoIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isDelimitador(char):
                if isOperadorAritimetrico(lexema):
                    return self.automato.setEstado("OperadorAritimeticoCompleto")
                return self.automato.setEstado("CaractereInvalido") # depois trocar para o estado de simbolo
            
            if ( maybeOperadorAritimetrico(lexema) ):
                return self.automato.setEstado("OperadorAritimeticoIncompleto")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isOperadorLogico(lexema):
            return self.automato.setEstado("OperadorAritimeticoCompleto")
        return self.automato.setEstado("CaractereInvalido") # depois trocar para o estado de simbolo