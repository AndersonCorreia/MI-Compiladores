from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from estruturaLexica import *

class CaractereInvalidoState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def getTipo(self):
        return "simbolo invalido"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")