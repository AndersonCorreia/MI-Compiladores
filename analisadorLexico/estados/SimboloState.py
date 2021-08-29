from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *

class SimboloState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("Simbolo")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "simbolo"
    
    def getSigla(self):
        return "SIB"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("Simbolo")