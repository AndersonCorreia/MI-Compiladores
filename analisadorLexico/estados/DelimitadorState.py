from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class DelimitadorState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("TokenVazio")
        
    def caractereCompoemLexema(self):
        return True
    
    def getTipo(self):
        return "delimitador"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")