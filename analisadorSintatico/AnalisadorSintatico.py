from gramatica import *

class AnalisadorSintatico:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.token = None
        
    def proximoToken(self):
        if len(self.tokens) > 0:
            self.token = self.token = self.tokens[0]
        else:
            self.token = None
    
    def analisarSintaxe(self):
        
        self.proximoToken()
        self.program()
        
        print("pilha : \n")
        print(self.tokens)
        
    def match(self, tipo, lexema = None):
        """
        Método que verificar se o token atual é compativel com o fornecido.
        
        Parameters:
            tipo (str): tipo do token de acordo as siglas usadas no lexico
            
            lexema (str|number): lexema do token, se None significa que não é necessário verificar conteudo do lexema
        """
        
        if self.token['tipo'] == tipo:
            if lexema == None or self.token['lexema'] == lexema:
                self.tokens.pop(0)
                self.proximoToken()
                return True
        
        if lexema == None:
            lexema = ''
        raise Exception('Erro sintático', 'Esperado: ' + tipo + ' ' + lexema + ', Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])
    
    def program(self):
        self.type()#teste reconhecendo se no arquivo existe apenas um token do tipo type
        
    def type(self):
        
        if( proximo("primitive_type", self.token) ):
            self.primitive_type()
        else:
            self.match("IDE")
            
    def primitive_type(self):
        
        if self.token['lexema'] == 'inteiro':
            self.match("PRE", "inteiro")
        elif self.token['lexema'] == 'real':
            self.match("PRE", "real")
        elif self.token['lexema'] == 'char':
            self.match("PRE", "char")
        elif self.token['lexema'] == 'booleano':
            self.match("PRE", "booleano")
        elif self.token['lexema'] == 'cadeia':
            self.match("PRE", "cadeia")
        elif self.token['lexema'] == 'vazio':
            self.match("PRE", "vazio")
        else:
            print(self.token)
            raise Exception('Erro sintático', 'Esperado: inteiro, real, char, booleano, cadeia, vazio, Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])