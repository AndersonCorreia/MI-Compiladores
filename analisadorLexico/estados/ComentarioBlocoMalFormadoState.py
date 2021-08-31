from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *

class ComentarioBlocoMalFormadoState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("ComentarioBlocoMalFormado")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "Comentario mal formado"
    
    def getSigla(self):
        return "CoMF"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")
    
    def pularDelimitadorSemToken(self):
        return False