from os import error
from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Funcao:

    def main_function(self):
        try:
            if primeiro("function_parameters", self.token):
                self.function_parameters()
                self.match("DEL", "{", proximoNT="function_body")
                self.function_body()
                self.match("DEL", "}")
                if not self.tabelaDeSimbolos.addFunction(self.semanticoHelper['functionNameToken'], self.semanticoHelper['functionParameters'], self.semanticoHelper['functionReturn']):
                    self.registrarErrosSemanticos()
            else:
                erro = "Tokens ou Não-Terminais Esperados function_parameters"
                self.registrarErro(erro)
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("main_function", self.token):
                    return self.main_function()
                elif sequinte("main_function", self.token):
                    return
                else:
                    self.tokensIgnorados.append(self.token)
                    self.proximoToken()   

    def function_body(self):
        try:
            if primeiro("declaration_const", self.token):
                self.declaration_const()
                self.function_body1()
            elif primeiro("function_body1", self.token):
                self.function_body1()
            else:
                erro = "Tokens ou Não-Terminais Esperados declaration_const ou function_body1"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_body", self.token):
                return self.function_body()
            elif sequinte("function_body", self.token):
                return
            else:
                raise e

    def function_body1(self):
        try:
            if primeiro("declaration_var", self.token):
                self.declaration_var()
                self.function_body2()
            elif primeiro("function_body2", self.token):
                self.function_body2()
            else:
                erro = "Tokens ou Não-Terminais Esperados declaration_var ou function_body2"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_body1", self.token):
                return self.function_body1()
            elif sequinte("function_body1", self.token):
                return
            else:
                raise e

    def function_body2(self):
        try:
            if primeiro("com_enquanto", self.token):
                self.com_enquanto()
                self.function_body2()
            elif primeiro("com_para", self.token):
                self.com_para()
                self.function_body2()
            elif primeiro("se", self.token):
                self.se()
                self.function_body2()
            elif primeiro("write_cmd", self.token):
                self.write_cmd()
                self.function_body2()
            elif primeiro("read_cmd", self.token):
                self.read_cmd()
                self.function_body2()
            elif primeiro("functionCall", self.token) and self.tokens[1]['lexema'] == '(':
                self.functionCall()
                self.function_body2()
            elif primeiro("var_atr", self.token):
                self.var_atr()
                self.function_body2()
            elif primeiro("retornar", self.token):
                self.retornar()
            else:
                erro = "Tokens ou Não-Terminais Esperados com_enquanto, com_para, se, write_cmd, read_cmd, functionCall, var_atr ou retornar"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_body2", self.token):
                return self.function_body2()
            elif sequinte("function_body2", self.token):
                return
            else:
                raise e

    def retornar(self):
        try:
            if(self.token['lexema'] == 'retorno'):
                self.match("PRE", "retorno", proximoNT="retornar1")
                self.retornar1()
                self.match("DEL", ";")
            else:
                erro = "Tokens ou Não-Terminais Esperados 'retorno'"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("retornar", self.token):
                return self.retornar()
            elif sequinte("retornar", self.token):
                return
            else:
                raise e

    def retornar1(self):
        try:
            if primeiro("value_with_expressao", self.token):
                self.value_with_expressao()
            else:
                return # declaração vazia
        except Exception as e:
            if primeiro("retornar1", self.token):
                return self.retornar1()
            elif sequinte("retornar1", self.token):
                return
            else:
                raise e

    def function_parameters(self):
        try:
            if(self.token['lexema'] == '('):
                self.match("DEL", "(", proximoNT="function_parameters1")
                self.function_parameters1()
            else:
                erro = "Tokens ou Não-Terminais Esperados '('"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_parameters", self.token):
                return self.function_parameters()
            elif sequinte("function_parameters", self.token):
                return
            else:
                raise e

    def function_parameters1(self):
        try:
            if primeiro("type", self.token):
                self.salvarTokenTemp = True
                self.type()
                self.semanticoHelper['functionParameters'].append(self.tokenTemp['lexema'])
                self.salvarTokenTemp = False
                self.match("IDE", proximoNT="function_parameters2")
                self.function_parameters2()
            elif self.token['lexema'] == ')':
                self.match("DEL", ")")
            else:
                erro = "Tokens ou Não-Terminais Esperados type ou ')'"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_parameters1", self.token):
                return self.function_parameters1()
            elif sequinte("function_parameters1", self.token):
                return
            else:
                raise e

    def function_parameters2(self):
        try:
            if(self.token['lexema'] == '[' ):
                self.match( "DEL", '[')
                self.match( "DEL", ']', proximoNT="function_parameters3")
                self.function_parameters3()
            elif primeiro("function_parameters4", self.token):
                self.function_parameters4()
            else:
                erro = "Tokens ou Não-Terminais Esperados '[' ou function_parameters4"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_parameters2", self.token):
                return self.function_parameters2()
            elif sequinte("function_parameters2", self.token):
                return
            else:
                raise e

    def function_parameters3(self):
        try:
            if(self.token['lexema'] == '[' ):
                self.match( "DEL", '[')
                self.match( "DEL", ']', proximoNT="function_parameters4")
                self.function_parameters4()
            elif primeiro("function_parameters4", self.token):
                self.function_parameters4()
            else:
                erro = "Tokens ou Não-Terminais Esperados ']' ou function_parameters4"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_parameters3", self.token):
                return self.function_parameters3()
            elif sequinte("function_parameters3", self.token):
                return
            else:
                raise e

    def function_parameters4(self):
        try:
            if(self.token['lexema'] == ',' ):
                self.match("DEL", ",", proximoNT="function_parameters1")
                self.function_parameters1()
            elif self.token['lexema'] == ')':
                self.match("DEL", ")")
            else:
                erro = "Tokens ou Não-Terminais Esperados ')' ou function_parameters1"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_parameters4", self.token):
                return self.function_parameters4()
            elif sequinte("function_parameters4", self.token):
                return
            else:
                raise e

    def function_declaration(self):
        try:
            self.semanticoHelper['functionReturn'] = None
            self.semanticoHelper['functionParameters'] = []
            if(self.token['lexema'] == 'funcao'):
                self.tabelaDeSimbolos.deleteVarsAndConstsEscopoLocal()
                self.match("PRE", "funcao", proximoNT="type")
                self.salvarTokenTemp = True
                self.type()
                self.semanticoHelper['functionReturn'] = self.tokenTemp['lexema']
                self.salvarTokenTemp = False
                self.function_declaration1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: 'funcao'"
                self.registrarErro(erro)
        except Exception as e:
            # while self.token['tipo'] != 'EOF':
            #     if primeiro("function_declaration", self.token):
            #         return self.function_declaration()
            #     elif sequinte("function_declaration", self.token):
            #         return
            #     else:
            #         self.tokensIgnorados.append(self.token)
            #         self.proximoToken()
            raise e
    
    def function_declaration1(self):
        try:
            self.semanticoHelper['functionNameToken'] = None
            if(self.token['lexema'] == 'algoritmo'):
                self.salvarTokenTemp = True
                self.match("PRE", "algoritmo", proximoNT="main_function")
                self.semanticoHelper['functionNameToken'] = self.tokenTemp
                self.salvarTokenTemp = False
                self.main_function()
            elif( primeiro("function_declaration2", self.token) ):
                self.function_declaration2()
            else:
                erro = "Tokens ou Não-Terminais Esperados: 'algoritmo' ou function_declaration2"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_declaration1", self.token):
                return self.function_declaration1()
            elif sequinte("function_declaration1", self.token):
                return
            else:
                raise e
    
    def function_declaration2(self):
        try:
            if(self.token['tipo'] == 'IDE'):
                self.salvarTokenTemp = True
                self.match("IDE", proximoNT="function_parameters")
                self.semanticoHelper['functionNameToken'] = self.tokenTemp
                self.salvarTokenTemp = False
                self.function_parameters()
                self.match("DEL", "{", proximoNT="function_body")
                self.function_body()
                self.match("DEL", "}", proximoNT="function_declaration")
                if not self.tabelaDeSimbolos.addFunction(self.semanticoHelper['functionNameToken'], self.semanticoHelper['functionParameters'], self.semanticoHelper['functionReturn']):
                    self.registrarErrosSemanticos()
                self.function_declaration()
            else:
                erro = "Tokens ou Não-Terminais Esperados: IDE"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("function_declaration2", self.token):
                return self.function_declaration2()
            elif sequinte("function_declaration2", self.token):
                return
            else:
                raise e
    
    def functionCall(self):
        try:
            if(self.token['tipo'] == 'IDE'):
                self.salvarTokenTemp = True
                self.match("IDE", proximoToken={"tipo": "DEL", "lexema": "("})
                self.semanticoHelper['functionCallNameToken'] = self.tokenTemp
                self.salvarTokenTemp = False
                self.match("DEL", "(", proximoNT="varList0")
                self.varList0()
                self.match("DEL", ")", proximoToken={"tipo": "DEL", "lexema": ";"})
                self.match("DEL", ";")
                if not self.tabelaDeSimbolos.callFunction(self.semanticoHelper['functionCallNameToken'], self.semanticoHelper['functionCallParameters']):
                    self.registrarErrosSemanticos()
            else:
                erro = 'Tokens e Não-Terminais Esperados: IDE'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("functionCall", self.token):
                return self.functionCall()
            elif sequinte("functionCall", self.token):
                return
            else:
                raise e

    def varList0(self):
        try:
            self.semanticoHelper['functionCallParameters'] = []
            if( primeiro("value", self.token) ):
                self.salvarTokenTemp = True
                self.value()
                self.salvarTokenTemp = False
                tipo = self.tabelaDeSimbolos.getTipoByToken(self.tokenTemp)
                self.semanticoHelper['functionCallParameters'].append(tipo)
                self.varList2
            elif( primeiro("read_value", self.token) ):
                self.read_value()
                key = self.semanticoHelper['tokenIDE']['lexema']
                if key in self.tabelaDeSimbolos.varConstTable:
                    tipo = self.tabelaDeSimbolos.varConstTable[key]['tipo']
                    self.semanticoHelper['functionCallParameters'].append(tipo)
                else:
                    self.semanticoHelper['functionCallParameters'].append('vazio')
                self.varList2
            else:
                return # declaração vazia
        except Exception as e:
            if primeiro("varList0", self.token):
                return self.varList0()
            elif sequinte("varList0", self.token):
                return
            else:
                raise e
    
    def varList1(self):
        try:
            if( primeiro("value", self.token) ):
                self.salvarTokenTemp = True
                self.value()
                self.salvarTokenTemp = False
                tipo = self.tabelaDeSimbolos.getTipoByToken(self.tokenTemp)
                self.semanticoHelper['functionCallParameters'].append(tipo)
                self.varList2
            elif( primeiro("read_value", self.token) ):
                self.read_value()
                key = self.semanticoHelper['tokenIDE']['lexema']
                if key in self.tabelaDeSimbolos.varConstTable:
                    tipo = self.tabelaDeSimbolos.varConstTable[key]['tipo']
                    self.semanticoHelper['functionCallParameters'].append(tipo)
                else:
                    self.semanticoHelper['functionCallParameters'].append('vazio')
                self.varList2
            else:
                erro = "Tokens ou Não-Terminais Esperados: value ou read_value"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("varList1", self.token):
                return self.varList1()
            elif sequinte("varList1", self.token):
                return
            else:
                raise e
    
    def varList2(self):
        try:
            if( self.token['lexema'] == ',' ):
                self.match("DEL", ",", proximoNT="varList1")
                self.varList1()
            else:
                return # declaração vazia
        except Exception as e:
            if primeiro("varList2", self.token):
                return self.varList2()
            elif sequinte("varList2", self.token):
                return
            else:
                raise e