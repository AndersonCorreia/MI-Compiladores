from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Para:
    
    def com_para(self):
        try:
            if( self.token['lexema'] == 'para'):
                self.match('PRE', 'para', proximoToken={'tipo':'DEL', 'lexema': '('})
                self.match('DEL', '(', proximoNT="init")
                self.init()
                self.stop()
                self.match('DEL', ';', proximoNT="step")
                self.step()
                self.match('DEL', ')', proximoToken={'tipo':'DEL', 'lexema': '{'})
                self.match('DEL', '{', proximoNT="com_body")
                self.match('DEL', '}')
            else:
                erro = "Tokens ou Não-Terminais Esperados: para"
                self.registrarErro(erro)
                
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("com_para", self.token):
                    return self.com_para()
                elif sequinte("com_para", self.token):
                    return
                else:
                    self.proximoToken()
            raise e
        
    def init(self):
        try:
            if( primeiro("var_atr", self.token) ):
                self.var_atr()
            elif( self.token['lexema'] == ';' ):
                self.match('DEL', ';')
            else:
                erro = "Tokens ou Não-Terminais Esperados: var_atr, ;"
                self.registrarErro(erro)
                
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("init", self.token):
                    return self.init()
                elif sequinte("init", self.token):
                    return
                else:
                    self.proximoToken()
            raise e
        
    def stop(self):
        try:
            if( primeiro("expressao", self.token) ):
                self.expressao()
            else:
                return # declaração vazia
                
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("stop", self.token):
                    return self.stop()
                elif sequinte("stop", self.token):
                    return
                else:
                    self.proximoToken()
            raise e
        
    def step(self):
        try:
            if( primeiro("var_atr", self.token) ):
                self.var_atr()
            elif( primeiro('expr_number', self.token) ):
                self.expr_number()
            else:
                return # declaração vazia
                
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("step", self.token):
                    return self.step()
                elif sequinte("step", self.token):
                    return
                else:
                    self.proximoToken()
            raise e
    