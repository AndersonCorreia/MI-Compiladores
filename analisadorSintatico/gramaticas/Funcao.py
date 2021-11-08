from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Funcao:
    
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