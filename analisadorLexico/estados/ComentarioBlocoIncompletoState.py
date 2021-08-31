from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class ComentarioBlocoIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if char == "#":
            return self.automato.setEstado("ComentarioBlocoIncompleto")
        #return self.automato.setEstado("Delimitador")
                    
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("ComentarioBlocoIncompleto")
    
    def pularDelimitadorSemToken(self):
        return False