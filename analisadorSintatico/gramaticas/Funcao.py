from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Funcao:

    def main_function(self):
        pass

    def function_body(self):
        pass

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
                erro = "Esperado: 'funcao'"
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
                erro = "Esperado: 'algoritmo' ou function_declaration2"
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
                erro = "Esperado: IDE"
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
                erro = 'Esperado: IDE'
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
                erro = "Esperado: value ou read_value"
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