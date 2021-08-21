from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class IndentificadorOuPalavraReservadaState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isLetraDigito(char) or char == '_':
                if maybePalavraReservada(lexema):
                    return self.automato.setEstado("IndentificadorOuPalavraReservada")
                
                return self.automato.setEstado("IndentificadorIncompleto")
            
            if isDelimitador(char):
                if isPalavraReservada(lexema):
                    return self.automato.setEstado("PalavraReservada")
                return self.automato.setEstado("IndentificadorCompleto")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isPalavraReservada(lexema):
            return self.automato.setEstado("PalavraReservada")
        return self.automato.setEstado("IndentificadorCompleto")