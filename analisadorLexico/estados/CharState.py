from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class CharState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("AguardandoDelimitador")
        
    def caractereCompoemLexema(self):
        return True
    
    def getTipo(self):
        return "Caractere"
    
    def getSigla(self):
        return "CAR"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("Char")