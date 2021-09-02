from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class OperadorAritimetricoIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isDelimitador(char):
                if isOperadorAritimetrico(lexema):
                    return self.automato.setEstado("OperadorAritimetricoCompleto")
                if isOperadorLogico(lexema):
                    return self.automato.setEstado("OperadorLogicoCompleto")
                if isOperadorRelacional(lexema):
                    return self.automato.setEstado("OperadorRelacionalCompleto")
                return self.automato.setEstado("OperadorMalFormado")
            
            if ( maybeOperadorAritimetrico(lexema) ):
                return self.automato.setEstado("OperadorAritimetricoIncompleto")
        
        if char == "\"":
            return self.automato.setEstado("OperadorMalFormadoString")
         
        if char == "\'":
            return self.automato.setEstado("OperadorMalFormadoChar")  
        
        return self.automato.setEstado("OperadorMalFormado")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isOperadorAritimetrico(lexema):
            return self.automato.setEstado("OperadorAritimetricoCompleto")
        return self.automato.setEstado("OperadorMalFormado")