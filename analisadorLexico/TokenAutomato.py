from estados.TokenVazioState import TokenVazioState
from estruturaLexica import *

class TokenAutomato:
    
    def __init__(self, fileName):
        self.estado = TokenVazioState
        self.file = open(fileName, 'r')
        self.tokens = []
        self.errors = []
        self.lexemaAtual = ""
        self.linhaAtual = 1
        
    def analisarArquivo(self):
        line = self.file.readline()
        while line:
            for pos in range(len(line)):
                char = line[pos]
                self.estado = self.estado.getProximoEstado(char, self.lexemaAtual)
                
                if self.estado.caractereCompoemLexema():
                    self.lexemaAtual += char
                else:
                    pos = pos - 1 #para analisar posteriomente em outro token
                    
                if self.estado.lexemaCompleto():
                    self.tokens.append(self.getToken())
                    self.lexemaAtual = ""
                    self.estado = TokenVazioState
                if self.estado.isError:
                    while not isDelimitador(char):
                        pos += 1
                        char = line[pos]
                        self.lexemaAtual += char
                        
                    self.errors.append(self.getError())
                    self.lexemaAtual = ""
                    self.estado = TokenVazioState
                
            self.linhaAtual += 1
            line = self.file.readline()
            
    def getToken(self):
        token = { 
                'lexema': self.lexemaAtual, 
                'linha': self.linhaAtual, 
                'tipo': self.estado.getTipo(), 
                'metadados': self.estado.getMetadados() 
                }
        return token
    
    def getError(self):
        error = {
                'lexema': self.lexemaAtual,
                'linha': self.linhaAtual, 
                'tipo': self.estado.getTipo(), 
                'metadados': self.estado.getMetadados() 
                }
        return error
    
    def isDelimitador(self, char):
        return self.estado.isDelimitador(char)
    