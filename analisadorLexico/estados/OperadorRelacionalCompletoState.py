from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from analisadorLexico.estruturaLexica import *

class OperadorRelacionalCompletoState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            return self.automato.setEstado("AguardandoDelimitador")
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "operador relacional"
    
    def getSigla(self):
        return "REL"
    
    def finalDoArquivo(self, lexema):
        return self.automato.setEstado("TokenVazio")