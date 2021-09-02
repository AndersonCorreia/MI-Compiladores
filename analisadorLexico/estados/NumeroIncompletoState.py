from analisadorLexico.estados.interfaces.EstadoAbertoInterface import EstadoAbertoInterface
from estruturaLexica import *

class NumeroIncompletoState(EstadoAbertoInterface):
    
    def getProximoEstado(self, char, lexema):
        if isSimboloPermitido(char):
            if isDigito(char) or char == ".":
                quantidadeDePontos = lexema.count(".")
                if quantidadeDePontos > 1:
                    return self.automato.setEstado("NumeroMalFormado")
                return self.automato.setEstado("NumeroIncompleto")
            if isDelimitador(char):
                quantidadeDePontos = lexema.count(".")
                if quantidadeDePontos <= 1 and lexema[-1] != ".":
                    return self.automato.setEstado("NumeroCompleto")
            return self.automato.setEstado("NumeroMalFormado")
            
        return self.automato.setEstado("CaractereInvalido")
        
    def caractereCompoemLexema(self):
        return True
    
    def finalDoArquivo(self,  lexema ):
        return self.automato.setEstado("NumeroCompleto")