from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from analisadorLexico.estruturaLexica import *

class StringState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("tokenVazio")
        
    def caractereCompoemLexema(self):
        return True
    
    def getTipo(self):
        return "Cadeia de caracteres"
    
    def getSigla(self):
        return "CAD"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("String")