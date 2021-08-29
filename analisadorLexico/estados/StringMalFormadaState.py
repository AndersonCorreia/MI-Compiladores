from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *

class StringMalFormadaState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("StringMalFormada")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "simbolo invalido"
    
    def getSigla(self):
        return "CMF"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")
    
    def isLexemaErrorCompleto(self, char, lexema):
        return lexema[-1] == '"' or char == '\n'
    
    def pularDelimitadorSemToken(self):
        return False