from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class OperadorLogicoIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isDelimitador(char):
                if isOperadorLogico(lexema):
                    return self.automato.setEstado("OperadorLogicoCompleto")
                return self.automato.setEstado("OperadorMalFormado")
            
            if ( maybeOperadorLogico(lexema) ):
                return self.automato.setEstado("OperadorLogicoIncompleto")
         
        if char == "\"":
            return self.automato.setEstado("OperadorMalFormadoString")
         
        if char == "\'":
            return self.automato.setEstado("OperadorMalFormadoChar")  
        
        return self.automato.setEstado("OperadorMalFormado")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isOperadorLogico(lexema):
            return self.automato.setEstado("OperadorLogicoCompleto")
        return self.automato.setEstado("OperadorMalFormado")