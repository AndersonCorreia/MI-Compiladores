from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from analisadorLexico.estruturaLexica import *

class ComentarioLinhaIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
      if char == "\n":
        return self.automato.setEstado("ComentarioLinha")
      return self.automato.setEstado("ComentarioLinhaIncompleto")
                    
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("ComentarioLinhaIncompleto")
    
    def pularDelimitadorSemToken(self):
        return False