from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from analisadorLexico.estruturaLexica import *

class CharIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char) or char == "'":
            if  (3 > len(lexema) or len(lexema) > 4) and char == "\n":
                return self.automato.setEstado("CharMalFormado")
            if (char != "'" and len(lexema) < 2 ) or (lexema[-1] == "\\" and len(lexema) < 3):
                return self.automato.setEstado("CharIncompleto")
            if char == "'" and (len(lexema) == 2 or (lexema == "'\\'" and len(lexema) == 3) ) or (isDelimitador(char) and lexema == "'\\'"):
                return self.automato.setEstado("Char")
            return self.automato.setEstado("CharMalFormado")
            
        return self.automato.setEstado("CharMalFormado")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema):
        return self.automato.setEstado("CharMalFormado")
    
    def pularDelimitadorSemToken(self):
        return False