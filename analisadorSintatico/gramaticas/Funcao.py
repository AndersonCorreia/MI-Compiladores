from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Funcao:

    def main_function(self):
        try:
            if primeiro("function_parameters", self.token):
                self.function_parameters()
                self.match("DEL", "{", proximoNT="function_body")
                self.function_body()
                self.match("DEL", "}")
            else:
                erro = "Esperado: parametros da função"
                self.registrarErro(erro)
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("main_function", self.token):
                    return self.main_function()
                elif sequinte("main_function", self.token):
                    return
                else:
                    raise e    

    def function_body(self):
        try:
            if primeiro("declaration_const", self.token):
                self.declaration_const()
                self.function_body1()
            else:
                self.function_body1()
        except Exception as e:
            while self.token['tipo'] != 'EOF':
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
            else:
                self.function_body2()
        except Exception as e:
            while self.token['tipo'] != 'EOF':
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
            elif primeiro("functionCall", self.token):
                self.functionCall()
                self.function_body2()
            elif primeiro("var_atr", self.token):
                self.var_atr()
                self.function_body2()
            else:
                self.retornar()
        except Exception as e:
            while self.token['tipo'] != 'EOF':
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
                erro = "Esperado: '('"
                self.registrarErro(erro)
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("retornar", self.token):
                    return self.retornar()
                elif sequinte("retornar", self.token):
                    return
                else:
                    raise e

    def retornar1(self):
        try:
            if primeiro("com_retornar1", self.token):
                self.com_retornar1()
            else:
                erro = "Esperado: cadeia, char ou expressão"
                self.registrarErro(erro)
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("retornar1", self.token):
                    return self.retornar1()
                elif sequinte("retornar1", self.token):
                    return
                else:
                    raise e

    def function_parameters(self):
        try:
            if(self.token['lexema'] == '('):
                self.match("DEL", "(", proximoNT="type")
                self.type()
                self.function_parameters1()
            else:
                erro = "Esperado: '('"
                self.registrarErro(erro)
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("function_parameters", self.token):
                    return self.function_parameters()
                elif sequinte("function_parameters", self.token):
                    return
                else:
                    self.tokensIgnorados.append(self.token)
                    self.proximoToken()
            raise e

    def function_parameters1(self):
        try:
            if primeiro("type", self.token):
                self.type()
                self.match("IDE", proximoNT="type")
                self.function_parameters2()
                self.match("DEL", ")")
            else:
                erro = "Esperado: tipo primitivo ou identificador"
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
                return
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
                self.match( "DEL", '[',)
                self.match( "DEL", ']')
                self.function_parameters4()
            elif primeiro("function_parameters4", self.token):
                self.function_parameters4()
            else:
                erro = "Esperado: lexema ']'"
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
                self.match("DEL", ",", proximoNT={"function_parameters1"})
                self.function_parameters1()
            else:
                erro = "Esperado: lexema ']'"
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
            if(self.token['lexema'] == 'funcao'):
                self.match("PRE", "funcao", proximoNT="type")
                self.type()
                self.function_declaration1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: 'funcao'"
                self.registrarErro(erro)
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("function_declaration", self.token):
                    return self.function_declaration()
                elif sequinte("function_declaration", self.token):
                    return
                else:
                    self.tokensIgnorados.append(self.token)
                    self.proximoToken()
            raise e
    
    def function_declaration1(self):
        try:
            if(self.token['lexema'] == 'algoritmo'):
                self.match("PRE", "algoritmo", proximoNT="main_function")
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
                self.match("IDE", proximoNT="function_parameters")
                self.function_parameters()
                self.match("DEL", "{", proximoNT="function_body")
                self.function_body()
                self.match("DEL", "}", proximoNT="function_declaration")
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
                self.match("IDE", proximoToken={"tipo": "DEL", "lexema": "("})
                self.match("DEL", "(", proximoNT="varList0")
                self.varList0()
                self.match("DEL", ")", proximoToken={"tipo": "DEL", "lexema": ";"})
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
            if( primeiro("value", self.token) ):
                self.value()
                self.varList2
            elif( primeiro("read_value", self.token) ):
                self.read_value()
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
                self.value()
                self.varList2
            elif( primeiro("read_value", self.token) ):
                self.read_value()
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