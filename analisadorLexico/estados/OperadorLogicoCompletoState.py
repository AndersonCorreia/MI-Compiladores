from analisadorLexico.estados.interfaces.EstadoCompletoInterface import EstadoCompletoInterface
from estruturaLexica import *

class OperadorLogicoCompletoState(EstadoCompletoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            return self.automato.setEstado("AguardandoDelimitador")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return False
    
    def getTipo(self):
        return "operador logico"
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("TokenVazio")