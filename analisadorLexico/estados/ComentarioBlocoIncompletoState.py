from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class ComentarioBlocoIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if char == "}" and lexema[-1] == "#":
            return self.automato.setEstado("ComentarioBlocoCompleto")
        if lexema == "{" and char != "#":
            return self.automato.setEstado("Delimitador", True, False)
        return self.automato.setEstado("ComentarioBlocoIncompleto")
                    
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("ComentarioBlocoMalFormado")
    
    def pularDelimitadorSemToken(self):
        return False