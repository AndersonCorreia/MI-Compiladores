from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class IndentificadorCompletoState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("AguardandoDelimitador")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "identificador"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("IndentificadorCompleto")