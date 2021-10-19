from analisadorSintatico.regras.constantes import Constantes
from analisadorSintatico.regras.variaveis import Variaveis
from gramatica import *

class AnalisadorSintatico:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.token = None
        
    def proximoToken(self):
        if len(self.tokens) > 0:
            self.token = self.token = self.tokens[0]
        else:
            self.token = {'tipo': 'EOF', 'lexema': ''} #fim dos tokens
    
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
        self.declaracao_reg()
        self.contantes()
        self.variaveis()
    
    def declaracao_reg(self):
        
        if( self.token['lexema'] == 'registro' ):
            self.match("PRE", "registro")
            self.match("IDE")
            self.match("DEL", "{")
            self.declaracao_reg1()
        else:
            return # declaração vazia
        
    def declaracao_reg1(self):
        
        if( proximo("type", self.token) ):
            self.type()
            self.match("IDE")
            #self.declaracao_reg4() array falta fazer
            self.declaracao_reg2()
        else:
            raise Exception('Erro sintático', 'Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])
         
    def declaracao_reg2(self):
        
        if( self.token['lexema'] == ',' ):
            self.match("DEL", ",")
            self.match("IDE")
            self.declaracao_reg2()
        elif( self.token['lexema'] == ';' ):
            self.match("DEL", ";")
            self.declaracao_reg3()
        else:
            raise Exception('Erro sintático', 'Esperado: , ou ;, Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])
        
    def declaracao_reg3(self):
        
        if( self.token['lexema'] == '}' ):
            self.match("DEL", "}")
            self.declaracao_reg()
        elif( proximo("declaracao_reg1", self.token) ):
            self.declaracao_reg1()
        else:
            raise Exception('Erro sintático', 'Encontrados: ' + self.token['tipo'] + ' ' + self.token['lexema'])
        
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

    def contantes(self):
        Constantes.start()

    def variaveis(self):
        Variaveis.start()