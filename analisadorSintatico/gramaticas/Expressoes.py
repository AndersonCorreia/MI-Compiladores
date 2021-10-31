from analisadorSintatico.gramaticaHelper import primeiro, sequinte

class Expressoes:
    
    def expr_art(self):
        try:
            if ( primeiro("expr_multi") ):
                self.expr_multi()
                self.expr_art1()
            else:
                erro = "Esperado: expr_multi"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("expr_art", self.token):
                return self.expr_art()
            elif sequinte("expr_art", self.token):
                return
            else:
                raise e
            
    def expr_art1(self):
        try:
            if ( primeiro("operator_soma") ):
                self.operator_soma()
                self.expr_number()
            else:
                return # declaracao vazia
        except Exception as e:
            if primeiro("expr_art1", self.token):
                return self.expr_art1()
            elif sequinte("expr_art1", self.token):
                return
            else:
                raise e
    
    def operator_soma(self):
        try:
            if ( self.token['lexema'] == '+'):
                self.match('ART', '+')
            elif ( self.token['lexema'] == '-'):
                self.match('ART', '-')
            else:
                erro = "Esperado: + ou -"
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("operator_soma", self.token):
                return self.operator_soma()
            elif sequinte("operator_soma", self.token):
                return
            else:
                raise e
    
    def operator_multi(self):
        try:
            if ( self.token['lexema'] == '*'):
                self.match('ART', '*')
            elif ( self.token['lexema'] == '/'):
                self.match('ART', '/')
            else:
                erro = "Esperado: * ou /"
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("operator_multi", self.token):
                return self.operator_multi()
            elif sequinte("operator_multi", self.token):
                return
            else:
                raise e
    
    def operator_auto0(self):
        try:
            if ( self.token['lexema'] == '++'):
                self.match('ART', '++')
            elif ( self.token['lexema'] == '--'):
                self.match('ART', '--')
            else:
                erro = "Esperado: ++ ou --"
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("operator_auto0", self.token):
                return self.operator_auto0()
            elif sequinte("operator_auto0", self.token):
                return
            else:
                raise e
    
    def operator_auto(self):
        try:
            if ( self.token['lexema'] == '++'):
                self.match('ART', '++')
            elif ( self.token['lexema'] == '--'):
                self.match('ART', '--')
            else:
                return # declaracao vazia
                
        except Exception as e:
            if primeiro("operator_auto", self.token):
                return self.operator_auto()
            elif sequinte("operator_auto", self.token):
                return
            else:
                raise e
    
    def expr_valor_mod(self):
        try:
            if ( self.token['tipo'] == "NRO"):
                self.match("NRO")
            elif ( primeiro("operator_auto0") ):
                self.operator_auto0()
                self.read_value()
            elif ( primeiro("read_value") ):
                self.read_value()
                self.operator_auto0()
            else:
                erro = "Esperado: NRO, operator_auto0 ou read_value"
                self.registrarErro(erro)
            
        except Exception as e:
            if primeiro("expr_valor_mod", self.token):
                return self.expr_valor_mod()
            elif sequinte("expr_valor_mod", self.token):
                return
            else:
                raise e
    
    def expr_multi(self):
        try:
            if ( primeiro("operator_soma") ):
                self.operator_soma()
                self.expr_valor_mod()
                self.expr_multi_pos()
            elif ( primeiro("expr_valor_mod") ):
                self.expr_valor_mod()
                self.expr_multi_pos()
            else:
                erro = "Esperado: operator_soma, expr_valor_mod"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("expr_multi", self.token):
                return self.expr_multi()
            elif sequinte("expr_multi", self.token):
                return
            else:
                raise e
            
    def expr_multi_pos(self):
        try:
            if ( primeiro("operator_multi") ):
                self.operator_multi()
                self.expr_multi()
            else:
                return # declaracao vazia
        except Exception as e:
            if primeiro("expr_multi", self.token):
                return self.expr_multi()
            elif sequinte("expr_multi", self.token):
                return
            else:
                raise e
            
    def expr_number(self):
        try:
            if( primeiro("expr_art") ):
                self.expr_art()
            elif( self.token['lexema'] == '('):
                self.match('DEL', '(', proximoNT="expr_number")
                self.expr_number()
                self.match('DEL', '(', proximoNT="expr_multi_pos")
                self.expr_multi_pos()
                self.expr_number1()
            else:
                erro = "Esperado: expr_art ou '('"
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("expr_number", self.token):
                return self.expr_number()
            elif sequinte("expr_number", self.token):
                return
            else:
                raise e
    
    def expr_number1(self):
        try:
            if( primeiro("operator_soma") ):
                self.operator_soma()
                self.expr_number()
            else:
                return # declaracao vazia
                
        except Exception as e:
            if primeiro("expr_number1", self.token):
                return self.expr_number1()
            elif sequinte("expr_number1", self.token):
                return
            else:
                raise e
            