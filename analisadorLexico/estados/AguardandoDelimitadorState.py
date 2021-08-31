from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class AguardandoDelimitadorState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isDelimitador(char):
            if isDelimitadorSemToken(char):
                return self.automato.setEstado("TokenVazio")
            
            return self.automato.setEstado("Delimitador")
        return self.automato.setEstado("TokenVazio")
        
    def caractereCompoemLexema(self):
        return False
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")