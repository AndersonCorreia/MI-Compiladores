from analisadorLexico.estados.interfaces.EstadoDeErrorInterface import EstadoDeErrorInterface
from analisadorLexico.estruturaLexica import *

class CaractereInvalidoState(EstadoDeErrorInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "simbolo invalido"
    
    def getSigla(self):
        return "SII"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("CaractereInvalido")