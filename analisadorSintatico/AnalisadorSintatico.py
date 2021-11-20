from analisadorSintatico.gramaticas.Expressoes import Expressoes
from analisadorSintatico.gramaticas.Registro import Registro
from analisadorSintatico.gramaticas.Constantes import Constantes
from analisadorSintatico.gramaticas.Variaveis import Variaveis
from analisadorSintatico.gramaticas.SeSenao import SeSenao
from analisadorSintatico.gramaticas.VetoresMatrizes import VetoresMatrizes
from analisadorSintatico.gramaticas.Comando import Comando
from analisadorSintatico.gramaticas.Para import Para
from analisadorSintatico.gramaticas.Funcao import Funcao
from analisadorSintatico.gramaticas.Valor import Valor
from analisadorSintatico.gramaticas.Leia import Leia
from analisadorSintatico.gramaticas.Escreva import Escreva
from analisadorSintatico.SymbolTable import SymbolTable
from gramaticaHelper import *

class AnalisadorSintatico (Registro, Constantes, Variaveis, Expressoes, SeSenao, VetoresMatrizes, Comando, Para, Funcao, Valor, Leia, Escreva):
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.token = None
        self.salvarTokenTemp = False
        self.tokenTemp = None
        self.errors = []
        self.errorsSemanticos = []
        self.tokensIgnorados = []
        self.tabelaDeSimbolos = SymbolTable()
        # para colocar qualquer informação necessaria
        self.semanticoHelper = { "tokenEmAnalise": None}
        # campos uteis
        # semanticoHelper['v_m_access']['tipo'] informa se foi feito um acesso a array ou matriz na funcao v_m_access
        
    def getListaErrors(self):
        return self.errors
    
    def Program(self):
        
        try:
            self.declaracao_reg()
            self.declaration_const()
            self.declaration_var()
            self.function_declaration()
        except Exception as e:
            erro = "Erro inesperado ao analisar a gramatica"
            print(erro)
            print(e)
            while self.token['tipo'] != 'EOF':
                if primeiro("Program", self.token):
                    return self.Program()
                else:
                    self.tokensIgnorados.append(self.token)
                    self.proximoToken()
            # self.token['erro_sintatico'] = erro
            # self.errors.append(self.token)
    
    def proximoToken(self, removerToken = True):
        
        if removerToken and len(self.tokens) > 0:
            self.tokens.pop(0)
            
        if len(self.tokens) > 0:
            self.token = self.tokens[0]
        else:
            self.token = {'tipo': 'EOF', 'lexema': '', 'linha': 0} #fim dos tokens
    
    def analisarSintaxe(self):
        
        self.proximoToken(removerToken=False)
        self.Program()
        
        # print("pilha:")
        # print(self.tokens)
        # print("\nerros:")
        # print(self.errors)
        # print("\nQtd de tokens ignorados:")
        # print(len(self.tokensIgnorados))
        print("\nErros semanticos:\n")
        for erro in self.errorsSemanticos:
            print(erro)
        print("\nTabela de simbolos\n\nRegistros:\n")
        for key in self.tabelaDeSimbolos.structsTable:
            print("["+ key + "]")
            print(self.tabelaDeSimbolos.structsTable[key])
            print(" ")
        print("\nFunções:\n")
        for key in self.tabelaDeSimbolos.functionsTable:
            print("["+ key + "]")
            print(self.tabelaDeSimbolos.functionsTable[key])
            print(" ")
        
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
        
        erro = 'Tokens e Não-Terminais Esperados: ' + tipo
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
                if self.salvarTokenTemp:
                    self.tokenTemp = self.token
                self.proximoToken()
                return True
    
    def registrarErro(self, erro, raiseException = True):
        self.token['erro_sintatico'] = erro
        self.errors.append(self.token)
        erroMsg = erro + '; Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'"
        self.proximoToken()
        if raiseException:
            raise Exception('Erro sintático', erroMsg)
                
    def registrarErrosSemanticos(self):
        erros = self.tabelaDeSimbolos.getErros()
        for erro in erros:
            self._registrarErroSemantico(erro['erro'], erro['token'])
        
    def _registrarErroSemantico(self, erro, token):
        token['erro_semantico'] = erro
        self.errorsSemanticos.append(token)
                  
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
                erro = 'Tokens e Não-Terminais Esperados: inteiro, real, char, booleano, cadeia, vazio'
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
                erro = 'Tokens e Não-Terminais Esperados: read_value'
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
                erro = 'Tokens e Não-Terminais Esperados: value_with_expressao ou functionCall'
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
                erro = 'Tokens e Não-Terminais Esperados: , ou ;'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("atr_1", self.token):
                return self.atr_1()
            elif sequinte("atr_1", self.token):
                return
            else:
                raise e
            