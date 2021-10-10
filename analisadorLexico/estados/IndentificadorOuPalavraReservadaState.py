from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from analisadorLexico.estruturaLexica import *

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

            if isOperadorAritimetrico(char) or isOperadorRelacional(char) or isOperadorLogico(char):
                return self.automato.setEstado("OperadorMalFormadoChar")
                
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isPalavraReservada(lexema):
            return self.automato.setEstado("PalavraReservada")
        return self.automato.setEstado("IndentificadorCompleto")