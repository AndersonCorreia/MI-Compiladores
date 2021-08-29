from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class StringIncompletaState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char) or char == '"':
            if char == "\n":
                return self.automato.setEstado("StringMalFormada")
            if char != '"' or lexema[-1] == '\\':
                return self.automato.setEstado("StringIncompleta")
            return self.automato.setEstado("String")
            
        return self.automato.setEstado("StringMalFormada")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("StringMalFormada")
    
    def pularDelimitadorSemToken(self):
        return False