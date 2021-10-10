from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from analisadorLexico.estruturaLexica import *

class NumeroCompletoState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        return self.automato.setEstado("AguardandoDelimitador")

    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "numero"
    
    def getSigla(self):
        return "NRO"
    
    def finalDoArquivo(self,  lexema):
        return self.automato.setEstado("NumeroCompleto")