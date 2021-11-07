from analisadorSintatico.gramaticas.Expressoes import Expressoes
from analisadorSintatico.gramaticas.Registro import Registro
from analisadorSintatico.gramaticas.Constantes import Constantes
from analisadorSintatico.gramaticas.Variaveis import Variaveis
from analisadorSintatico.gramaticas.SeSenao import SeSenao
from analisadorSintatico.gramaticas.VetoresMatrizes import VetoresMatrizes
from analisadorSintatico.gramaticas.Comando import Comando
from gramaticaHelper import *

class AnalisadorSintatico (Registro, Constantes, Variaveis, Expressoes, SeSenao, VetoresMatrizes, Comando):
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.token = None
        self.erros = []
        self.tokensIgnorados = []
        
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
        print("\nQtd de tokens ignorados:")
        print(len(self.tokensIgnorados))
        
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
    
    def registrarErro(self, erro, raiseException = True):
        self.token['erro_sintatico'] = erro
        self.erros.append(self.token)
        erroMsg = erro + '; Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'"
        self.proximoToken()
        if raiseException:
            raise Exception('Erro sintático', erroMsg)
                
    def Program(self):
        
        try:
            self.se()
            # self.declaracao_reg()
            # self.contantes()
            # self.variaveis()
        except Exception as e:
            print("Erro na função principal: ")
            print(e)
            while self.token['tipo'] != 'EOF':
                if primeiro("Program", self.token):
                    return self.Program()
                else:
                    self.tokensIgnorados.append(self.token)
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
                erro = 'Esperado: inteiro, real, char, booleano, cadeia, vazio'
                self.registrarErro(erro)
                
            return
        except Exception as e:
            if primeiro("primitive_type", self.token):
                return self.primitive_type()
            elif sequinte("primitive_type", self.token):
                return
            
            raise Exception('Erro sintático', erro)
    
    def var_atr(self):
        try:
            if( primeiro("read_value", self.token)):
                self.read_value()
                self.match("REL", "=", proximoNT="atr_value")
                self.atr_value()
                self.atr_1()
            else:
                erro = 'Esperado: read_value'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("var_atr", self.token):
                return self.var_atr()
            elif sequinte("var_atr", self.token):
                return
            else:
                raise e
            
    def atr_value(self):
        try:
            if( primeiro("value_with_expressao", self.token)):
                self.value_with_expressao()
            elif( primeiro("functionCall", self.token)):
                self.functionCall()
            else:
                erro = 'Esperado: value_with_expressao ou functionCall'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("atr_value", self.token):
                return self.atr_value()
            elif sequinte("atr_value", self.token):
                return
            else:
                raise e
            
    def atr_1(self):
        try:
            if( self.token['lexema'] == ';' ):
                self.match("DEL", ";")
            elif( self.token['lexema'] == ',' ):
                self.match("DEL", ",", proximoNT="var_atr")
                self.var_atr()
            else:
                erro = 'Esperado: atr_1 ou atr_2'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("atr_1", self.token):
                return self.atr_1()
            elif sequinte("atr_1", self.token):
                return
            else:
                raise e
            