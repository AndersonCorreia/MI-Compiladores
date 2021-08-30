from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class ComentarioBlocoCompletoState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("AguardandoDelimitador")
        
    def caractereCompoemLexema(self):
        return True
    
    def getTipo(self):
        return "comentario de bloco"
    
    def getSigla(self):
        return "CMB"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("Comentario")