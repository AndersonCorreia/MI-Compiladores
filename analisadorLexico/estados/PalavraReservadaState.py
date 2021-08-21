from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class PalavraReservadaState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("AguardandoDelimitador")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "palavra reservada"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio") 