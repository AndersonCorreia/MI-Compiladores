from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *
from re import findall

class OperadorMalFormadoCharState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("OperadorMalFormadoChar")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "simbolo invalido"
    
    def getSigla(self):
        return "OpMF"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("OperadorMalFormadoChar")
    
    def isLexemaErrorCompleto(self, char, lexema):
        return len(findall("'",lexema)) == 2 or isDelimitadorSemToken(char)
    
    def pularDelimitadorSemToken(self):
        return False