from estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class TokenVazioState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):

        if char == '"':
            return self.automato.setEstado("StringIncompleta")
        
        if char == "'":
            return self.automato.setEstado("CharIncompleto")

        if isDigito(char):
            return self.automato.setEstado("NumeroIncompleto")
        
        if isSimboloPermitido(char):
            if isLetra(char):
                if maybePalavraReservada(lexema):
                    return self.automato.setEstado("IndentificadorOuPalavraReservada")
                return self.automato.setEstado("IndentificadorIncompleto")
            
            if maybeOperadorLogico(char):
                return self.automato.setEstado("OperadorLogicoIncompleto")
            
            if maybeOperadorAritimetrico(char):
                return self.automato.setEstado("OperadorAritimetricoIncompleto")
            
            if maybeOperadorRelacional(char):
                return self.automato.setEstado("OperadorRelacionalIncompleto")
            
            if maybeComentarioBloco(char):
                return self.automato.setEstado("ComentarioBlocoIncompleto")

            if isDelimitador(char):
                if isDelimitadorSemToken(char):
                    return self.automato.setEstado("TokenVazio")
                return self.automato.setEstado("Delimitador")

            if char == "%":
                return self.automato.setEstado("ComentarioLinhaIncompleto")

            return self.automato.setEstado("Simbolo")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return False
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")