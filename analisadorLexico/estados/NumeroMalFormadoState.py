from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *

class NumeroMalFormadoState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("NumeroMalFormado")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "numero mal formado"
    
    def getSigla(self):
        return "NMF"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("NumeroMalFormado")
    
    # def isLexemaErrorCompleto(self, char, lexema):
    #     return isDigito(lexema.split('.')[-1]) and lexema.count(".") > 1 
    
    def pularDelimitadorSemToken(self):
        return False