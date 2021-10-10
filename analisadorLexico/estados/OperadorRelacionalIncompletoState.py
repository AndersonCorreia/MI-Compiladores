from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from analisadorLexico.estruturaLexica import *

class OperadorRelacionalIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isDelimitador(char):
                if isOperadorRelacional(lexema):
                    return self.automato.setEstado("OperadorRelacionalCompleto")
                if isOperadorLogico(lexema):
                    return self.automato.setEstado("OperadorLogicoCompleto")
                if isOperadorAritimetrico(lexema):
                    return self.automato.setEstado("OperadorAritimetricoCompleto")
                
                return self.automato.setEstado("OperadorMalFormado")
            
            if ( maybeOperadorRelacional(lexema) ):
                return self.automato.setEstado("OperadorRelacionalIncompleto")
        
        if char == "\"":
            return self.automato.setEstado("OperadorMalFormadoString")
         
        if char == "\'":
            return self.automato.setEstado("OperadorMalFormadoChar")  
        
        return self.automato.setEstado("OperadorMalFormado")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        if isOperadorRelacional(lexema):
            return self.automato.setEstado("OperadorRelacionalCompleto")
        return self.automato.setEstado("OperadorMalFormado")