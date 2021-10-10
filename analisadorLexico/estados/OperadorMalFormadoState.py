from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from analisadorLexico.estruturaLexica import *
from re import findall

class OperadorMalFormadoState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("OperadorMalFormado")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "simbolo invalido"
    
    def getSigla(self):
        return "OpMF"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("OperadorMalFormado")
    
    def pularDelimitadorSemToken(self):
        return False