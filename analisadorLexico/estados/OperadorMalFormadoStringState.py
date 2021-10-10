from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from analisadorLexico.estruturaLexica import *
from re import findall

class OperadorMalFormadoStringState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("OperadorMalFormadoString")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "simbolo invalido"
    
    def getSigla(self):
        return "OpMF"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("OperadorMalFormadoString")
    
    def isLexemaErrorCompleto(self, char, lexema):
        return len(findall("\"",lexema)) == 2 or char == '\n'
    
    def pularDelimitadorSemToken(self):
        return False