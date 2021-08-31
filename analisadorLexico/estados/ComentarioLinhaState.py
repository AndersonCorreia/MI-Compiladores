from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class ComentarioLinhaState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("AguardandoDelimitador")
        
    def caractereCompoemLexema(self):
        return True
    
    def getTipo(self):
        return "comentario de linha"
    
    def getSigla(self):
        return "CML"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("ComentarioLinha")