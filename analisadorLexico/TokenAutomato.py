from analisadorLexico.estados.OperadorRelacionalCompletoState import OperadorRelacionalCompletoState
from analisadorLexico.estados.OperadorRelacionalIncompletoState import OperadorRelacionalIncompletoState
from analisadorLexico.estados.OperadorAritimetricoCompletoState import OperadorAritimetricoCompletoState
from analisadorLexico.estados.OperadorAritimetricoIncompletoState import OperadorAritimetricoIncompletoState
from analisadorLexico.estados.AguardandoDelimitadorState import AguardandoDelimitadorState
from analisadorLexico.estados.AusenciaDeDelimitadorState import AusenciaDeDelimitadorState
from analisadorLexico.estados.CaractereInvalidoState import CaractereInvalidoState
from analisadorLexico.estados.DelimitadorState import DelimitadorState
from analisadorLexico.estados.IndentificadorCompletoState import IndentificadorCompletoState
from analisadorLexico.estados.IndentificadorIncompletoState import IndentificadorIncompletoState
from analisadorLexico.estados.IndentificadorOuPalavraReservadaState import IndentificadorOuPalavraReservadaState
from analisadorLexico.estados.OperadorLogicoCompletoState import OperadorLogicoCompletoState
from analisadorLexico.estados.OperadorLogicoIncompletoState import OperadorLogicoIncompletoState
from analisadorLexico.estados.PalavraReservadaState import PalavraReservadaState
from analisadorLexico.estados.TokenVazioState import TokenVazioState
from estruturaLexica import *

class TokenAutomato:
    
    def __init__(self, fileName):
        self.file = open(fileName, 'r')
        self.tokens = []
        self.errors = []
        self.lexemaAtual = ""
        self.linhaAtual = 0
        self.setEstados()
        self.estado = self.estados["TokenVazio"]
        
    def setEstados(self):
        self.estados = {}
        self.estados["AguardandoDelimitador"] = AguardandoDelimitadorState(self)
        self.estados["AusenciaDeDelimitador"] = AusenciaDeDelimitadorState(self)
        self.estados["CaractereInvalido"] = CaractereInvalidoState(self)
        self.estados["Delimitador"] = DelimitadorState(self)
        self.estados["IndentificadorCompleto"] = IndentificadorCompletoState(self)
        self.estados["IndentificadorIncompleto"] = IndentificadorIncompletoState(self)
        self.estados["IndentificadorOuPalavraReservada"] = IndentificadorOuPalavraReservadaState(self)
        self.estados["OperadorLogicoCompleto"] = OperadorLogicoCompletoState(self)
        self.estados["OperadorLogicoIncompleto"] = OperadorLogicoIncompletoState(self)
        self.estados["OperadorAritimetricoCompleto"] = OperadorAritimetricoCompletoState(self)
        self.estados["OperadorAritimetricoIncompleto"] = OperadorAritimetricoIncompletoState(self)
        self.estados["OperadorRelacionalCompleto"] = OperadorRelacionalCompletoState(self)
        self.estados["OperadorRelacionalIncompleto"] = OperadorRelacionalIncompletoState(self)
        self.estados["PalavraReservada"] = PalavraReservadaState(self)
        self.estados["TokenVazio"] = TokenVazioState(self)
    
    def setEstado(self, estadoName):
        self.estado = self.estados[estadoName]
        
    def analisarArquivo(self):
        line = self.file.readline()
        while line:
            self.linhaAtual += 1
            pos = 0
            print(line)
            while pos < len(line):
                # print('pos: ' + str(pos))
                char = line[pos]
                # print('for')
                # print(self.estado)
                self.estado.getProximoEstado(char, self.lexemaAtual)
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
                        self.estado = self.estados["TokenVazio"]
                    else:
                        self.estado = self.estados["AguardandoDelimitador"]
                if self.estado.isError():
                    if not isDelimitador(char):
                        # print('linha: ' + line)
                        # print('pos: ' + str(pos))
                        # print('char: ' + char)
                        # print('lexema: ' + self.lexemaAtual)
                        self.lexemaAtual = self.lexemaAtual + char
                        pos = pos + 1
                    else:
                        self.errors.append(self.getError())
                        self.lexemaAtual = ""
                        self.estado = self.estados["TokenVazio"]
                        
                
            line = self.file.readline()
        self.fimDoArquivo()
    
    def fimDoArquivo(self):
        if self.lexemaAtual != "":
            self.estado.finalDoArquivo(self.lexemaAtual)
               
            if self.estado.lexemaCompleto():
                self.tokens.append(self.getToken())
            
            if self.estado.isError():
                self.errors.append(self.getError())
                
    def getToken(self):
        token = { 
                'lexema': self.lexemaAtual, 
                'linha': self.linhaAtual, 
                'tipo': self.estado.getSigla(),
                'metadados': self.estado.getMetadados() 
                }
        return token
    
    def getError(self):
        error = {
                'lexema': self.lexemaAtual,
                'linha': self.linhaAtual, 
                'tipo': self.estado.getSigla(), 
                'metadados': self.estado.getMetadados() 
                }
        return error
    
    def getListaTokens(self):
        return self.tokens
    
    def getListaErrors(self):
        return self.errors
    