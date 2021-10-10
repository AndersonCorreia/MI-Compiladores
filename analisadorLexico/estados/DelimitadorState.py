from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from analisadorLexico.estruturaLexica import *

class DelimitadorState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("TokenVazio")
        
    def caractereCompoemLexema(self):
        retorno = self.charCompoemLexema
        self.charCompoemLexema = True
        return retorno
    
    def getTipo(self):
        return "delimitador"
    
    def getSigla(self):
        return "DEL"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")
    
    def setCharCompoemLexema(self, compoem = True):
        self.charCompoemLexema = compoem