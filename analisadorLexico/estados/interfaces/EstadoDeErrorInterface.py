from analisadorLexico.estados.interfaces.EstadoInterface import EstadoInterface
from analisadorLexico.estruturaLexica import *

class EstadoDeErrorInterface(EstadoInterface):
    
    def lexemaCompleto(self):
        return False
    
    def isError(self):
        return True
    
    def isLexemaErrorCompleto(self, char, lexema):
        return isDelimitador(char)