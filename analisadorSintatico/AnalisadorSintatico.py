from analisadorSintatico.gramaticas.Registro import Registro
from analisadorSintatico.gramaticas.Constantes import Constantes
from analisadorSintatico.gramaticas.Variaveis import Variaveis
from gramaticaHelper import *

class AnalisadorSintatico (Registro, Constantes, Variaveis):
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.token = None
        self.erros = []
        
    def proximoToken(self, removerToken = True):
        
        if removerToken:
            self.tokens.pop(0)
            
        if len(self.tokens) > 0:
            self.token = self.tokens[0]
        else:
            self.token = {'tipo': 'EOF', 'lexema': ''} #fim dos tokens
    
    def analisarSintaxe(self):
        
        self.proximoToken(removerToken=False)
        self.Program()
        
        print("pilha:")
        print(self.tokens)
        print("\nerros:")
        print(self.erros)
        
    def match(self, tipo, lexema = None, proximoToken = None, proximoNT = None):
        """
        Método que verificar se o token atual é compativel com o fornecido.
        No caso de erro, analisa como processeguir com base no proximo token ou NT (apenas um deve ser fornecido)
        Parameters:
            tipo (str): tipo do token de acordo as siglas usadas no lexico
            
            lexema (str|number): lexema do token, se None significa que não é necessário verificar conteudo do lexema
            
            proximoToken (dict): tipo do token que deve seguir o token atual
            
            proximoNT (str): nome do NT que deve seguir o token atual
        """
        
        if self._match(tipo, lexema):
            return True
        
        erro = 'Esperado: ' + tipo
        if lexema != None:
            erro += ' ' + lexema
        self.registrarErro(erro)
        # erro registrado e a partir daqui se analisa como prosseguir a partir do token sequinte que virou o atual
        if self._match(tipo, lexema):#se o token atual dê match apenas retorna
            return True
        elif proximoToken != None:#se o token atual for o sequinte do esperado, então apenas retornar sem consumir o token
            if self.token['tipo'] == proximoToken['tipo'] and self.token['lexema'] == proximoToken['lexema']:
                return True
        elif proximoNT != None:#se o token atual fizer parte da lista primeiro do NT sequinte, então apenas retornar sem consumir o token
            if primeiro(proximoNT, self.token):
                return True
        #se essas condições não são atendidas um erro é lançado, para uma recuperação posterior
        
        raise Exception('Erro sintático', erro + ', Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
      
    def _match(self, tipo, lexema = None):
        
        if self.token['tipo'] == tipo:
            if lexema == None or self.token['lexema'] == lexema:
                self.proximoToken()
                return True
    
    def registrarErro(self, erro):
        self.token['erro_sintatico'] = erro
        self.erros.append(self.token)
        self.proximoToken()
                
    def Program(self):
        
        try:
            # self.type()#teste reconhecendo se no arquivo existe apenas um token do tipo type
            self.declaracao_reg()
            self.contantes()
            self.variaveis()
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("Program", self.token):
                    return self.Program()
                else:
                    self.proximoToken()
                  
    def contantes(self):
        consts = Constantes()
        consts.start()

    def variaveis(self):
        vars = Variaveis()
        vars.start()
        
    def type(self):
        
        try:
            if( primeiro("primitive_type", self.token) ):
                self.primitive_type()
            else:
                self.match("IDE")
        except Exception as e:
            if primeiro("type", self.token):
                return self.type()
            elif sequinte("type", self.token):
                return
            else:
                raise e
            
    def primitive_type(self):
        
        try:
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
                raise Exception('Erro sintático')
                
            return
        except Exception as e:
            erro = 'Esperado: inteiro, real, char, booleano, cadeia, vazio, Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema']
            self.registrarErro(erro)
            if primeiro("primitive_type", self.token):
                return self.primitive_type()
            elif sequinte("primitive_type", self.token):
                return
            
            raise Exception('Erro sintático', erro)
