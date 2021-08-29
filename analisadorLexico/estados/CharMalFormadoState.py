from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *

class CharMalFormadoState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("CharMalFormado")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "simbolo invalido"
    
    def getSigla(self):
        return "CaMF"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")
    
    def isLexemaErrorCompleto(self, char, lexema):
        return lexema[-1] == "'" or isDelimitadorSemToken(char)
    
    def pularDelimitadorSemToken(self):
        return False