from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class SeSenao:
    
    def se(self):
        try:
            if( self.token['lexema'] == 'se'):
                self.match('PRE', 'se', proximoToken={'tipo': 'PRE', 'lexema': '('})
                self.match('DEL', '(', proximoNT="expressao")
                self.expressao()
                self.match('DEL', ')', proximoToken={'tipo': 'PRE', 'lexema': '{'})
                self.match('DEL', '{', proximoNT="com_body")
                self.com_body()
                self.match('DEL', '}', proximoNT='se_body')
                self.se_body()
            else:
                erro = 'Tokens e Não-Terminais Esperados: se'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("se", self.token):
                return self.se()
            elif sequinte("se", self.token):
                return
            else:
                raise e
            
    def se_body(self):
        try:
            if( primeiro('senao', self.token)):
                self.senao()
            else:
                return # declaração vazia
        except Exception as e:
            if primeiro("se_body", self.token):
                return self.se_body()
            elif sequinte("se_body", self.token):
                return
            else:
                raise e
            
    def senao(self):
        try:
            if( self.token['lexema'] == 'senao'):
                self.match('PRE', 'senao', proximoNT="se_senao")
                self.se_senao()
            else:
                erro = 'Tokens e Não-Terminais Esperados: senao'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("senao", self.token):
                return self.senao()
            elif sequinte("senao", self.token):
                return
            else:
                raise e
            
    def se_senao(self):
        try:
            if( primeiro('se', self.token)):
                self.se()
            elif( self.token['lexema'] == '{'):
                self.match('DEL', '{', proximoNT="com_body")
                self.com_body()
                self.match('DEL', '}')
            else:
                erro = 'Tokens e Não-Terminais Esperados: se ou {'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("se_senao", self.token):
                return self.se_senao()
            elif sequinte("se_senao", self.token):
                return
            else:
                raise e