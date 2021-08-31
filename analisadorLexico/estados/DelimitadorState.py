from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class DelimitadorState(EstadoCompletoInterface):
    
    def __init__(self, fileName):
        self.charCompoemLexema = True
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("TokenVazio")
        
    def caractereCompoemLexema(self):
        return self.charCompoemLexema
    
    def getTipo(self):
        return "delimitador"
    
    def getSigla(self):
        return "DEL"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")