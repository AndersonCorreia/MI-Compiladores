from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Comando:
    
    def com_body(self):
        try:
            if( primeiro("com_enquanto", self.token) ):
                self.com_enquanto()
                self.com_body()
            elif( primeiro("com_para", self.token) ):
                self.com_para()
                self.com_body()
            elif( primeiro("se", self.token) ):
                self.se()
                self.com_body()
            elif( primeiro("write_cmd", self.token) ):
                self.write_cmd()
                self.com_body()
            elif( primeiro("read_cmd", self.token) ):
                self.read_cmd()
                self.com_body()
            elif( primeiro("functionCall", self.token) ):
                self.functionCall()
                self.com_body()
            elif( primeiro("var_atr", self.token) ):
                self.var_atr()
                self.com_body()
            elif( primeiro("com_retornar", self.token) ):
                self.com_retornar()
            else:
                erro = 'Esperado: enquanto, para, se, write_cmd, read_cmd, functionCall, var_atr, retorno'
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("com_body", self.token):
                return self.com_body()
            elif sequinte("com_body", self.token):
                return
            else:
                raise e
            
    def com_retornar(self):
        try:
            if( self.token['lexema'] == "retorno" ):
                self.match("PRE","retorno", proximoNT="com_retornar1")
                self.com_retornar1()
                self.match("DEL",";")
            else:
                return # declaração vazia
        except Exception as e:
            if primeiro("com_retornar", self.token):
                return self.com_retornar()
            elif sequinte("com_retornar", self.token):
                return
            else:
                raise e
            
    def com_retornar1(self):
        try:
            if( primeiro("value_with_expressao", self.token) ):
                self.value_with_expressao()
            else:
                return # declaração vazia
        except Exception as e:
            if primeiro("com_retornar1", self.token):
                return self.com_retornar1()
            elif sequinte("com_retornar1", self.token):
                return
            else:
                raise e
            
    def com_enquanto(self):
        try:
            if( primeiro("enquanto", self.token) ):
                self.match("PRE","enquanto", proximoToken={'tipo':'DEL', 'lexema':'('})
                self.match("DEL","(", proximoNT="args")
                self.args()
                self.match("DEL",")", proximoToken={'tipo':'DEL', 'lexema':'{'})
                self.match("DEL","{", proximoNT="com_body")
                self.com_body()
                self.match("DEL","}")
            else:
                erro = 'Esperado: enquanto'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("com_enquanto", self.token):
                return self.com_enquanto()
            elif sequinte("com_enquanto", self.token):
                return
            else:
                raise e
            
    def args(self):
        try:
            if( primeiro("expressao", self.token) ):
                self.expressao()
            else:
                return # declaração vazia
        except Exception as e:
            if primeiro("args", self.token):
                return self.args()
            elif sequinte("args", self.token):
                return
            else:
                raise e
    
    def read_value(self):
        try:
            if( self.token['tipo'] == "IDE"):
                self.match("IDE")
                self.read_value0()
            else:
                erro = 'Esperado: IDE'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("read_value", self.token):
                return self.read_value()
            elif sequinte("read_value", self.token):
                return
            else:
                raise e
    
    def read_value0(self):
        try:
            if( primeiro("v_m_access", self.token) ):
                self.v_m_access()
            elif( primeiro("elem_registro", self.token) ):
                self.elem_registro()
            else:
                return # declaração vazia
        except Exception as e:
            if primeiro("read_value0", self.token):
                return self.read_value0()
            elif sequinte("read_value0", self.token):
                return
            else:
                raise e