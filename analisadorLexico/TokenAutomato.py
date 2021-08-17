from analisadorLexico.estados.AguardandoDelimitadorState import AguardandoDelimitadorState
from analisadorLexico.estados.AusenciaDeDelimitadorState import AusenciaDeDelimitadorState
from analisadorLexico.estados.CaractereInvalidoState import CaractereInvalidoState
from analisadorLexico.estados.DelimitadorState import DelimitadorState
from analisadorLexico.estados.IndentificadorCompletoState import IndentificadorCompletoState
from analisadorLexico.estados.IndentificadorIncompletoState import IndentificadorIncompletoState
from analisadorLexico.estados.IndentificadorOuPalavraReservadaState import IndentificadorOuPalavraReservadaState
from analisadorLexico.estados.PalavraReservadaState import PalavraReservadaState
from analisadorLexico.estados.TokenVazioState import TokenVazioState
from estruturaLexica import *

class TokenAutomato:
    
    def __init__(self, fileName):
        self.estado = TokenVazioState
        self.file = open(fileName, 'r')
        self.tokens = []
        self.errors = []
        self.lexemaAtual = ""
        self.linhaAtual = 0
        
    def analisarArquivo(self):
        line = self.file.readline()
        while line:
            self.linhaAtual += 1
            pos = 0
            # print(line)
            while pos < len(line):
                # print('pos: ' + str(pos))
                char = line[pos]
                # print('for')
                # print(self.estado)
                self.estado = self.estado.getProximoEstado(char, self.lexemaAtual)
                # print('char: ' + char)
                # print('lexema: ' + self.lexemaAtual)
                # print(self.estado)
                if self.estado.caractereCompoemLexema():
                    self.lexemaAtual = self.lexemaAtual + char
                    pos = pos + 1
                    
                if isDelimitadorSemToken(char):
                    pos = pos + 1
                        
                if self.estado.lexemaCompleto():
                    self.tokens.append(self.getToken())
                    self.lexemaAtual = ""
                    if isDelimitador(char):
                        self.estado = TokenVazioState
                    else:
                        self.estado = AguardandoDelimitadorState
                if self.estado.isError():
                    while not isDelimitador(char):
                        pos = pos + 1
                        char = line[pos]
                        self.lexemaAtual += char
                        
                    self.errors.append(self.getError())
                    self.lexemaAtual = ""
                    self.estado = TokenVazioState
                
            line = self.file.readline()
        self.fimDoArquivo()
    
    def fimDoArquivo(self):
        if self.lexemaAtual != "":
            self.estado = self.estado.finalDoArquivo()
               
            if self.estado.lexemaCompleto():
                self.tokens.append(self.getToken())
            
            if self.estado.isError():
                self.errors.append(self.getError())
                
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
    
    def getListaTokens(self):
        return self.tokens
    