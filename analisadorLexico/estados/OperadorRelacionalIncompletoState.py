from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class OperadorRelacionalIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isDelimitador(char):
                if isOperadorRelacional(lexema):
                    return self.automato.setEstado("OperadorRelacionalCompleto")
                return self.automato.setEstado("CaractereInvalido") # depois trocar para o estado de simbolo
            
            if ( maybeOperadorRelacional(lexema) ):
                return self.automato.setEstado("OperadorRelacionalIncompleto")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isOperadorLogico(lexema):
            return self.automato.setEstado("OperadorRelacionalCompleto")
        return self.automato.setEstado("CaractereInvalido") # depois trocar para o estado de simbolo