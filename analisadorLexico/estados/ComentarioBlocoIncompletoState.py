from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class ComentarioBlocoIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char) or char == '#':
            if char == "\n":
                return self.automato.setEstado("ComentarioBlocoMalFormado")
            if char != '"' or lexema[-1] == '\\':
                return self.automato.setEstado("ComentarioBlocoIncompleto")
            return self.automato.setEstado("Comentario")
            
        return self.automato.setEstado("ComentarioBlocoMalFormado")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("ComentarioBlocoMalFormado")
    
    def pularDelimitadorSemToken(self):
        return False