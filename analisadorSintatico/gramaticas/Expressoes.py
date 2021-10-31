class Expressoes:
    
    def expressao(self):
        try:
            if( primeiro("expr_rel") ):
                self.expr_rel()
                self.expr_log1()
            elif( self.token['lexema'] == '('):
                self.match('DEL', '(', proximoNT="expressao")
                self.expressao()
                self.match('DEL', ')')
                self.expr_log2()
            elif( self.token['lexema'] == '!'):
                self.match('DEL', '!', proximoNT="expressao")
                self.expressao()
            else:
                erro = "Esperado: expr_rel ou '(' ou '!'"
                self.registrarErro(erro)
                
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("expressao", self.token):
                    return self.expressao()
                elif sequinte("expressao", self.token):
                    return
                else:
                    self.proximoToken()
            raise e
    
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
    
    def expr_rel(self):
        try:
            if( primeiro("expr_art") ):
                self.expr_art()
                self.expr_rel1()
            elif( self.token['PRE'] == 'verdadeiro'):
                self.match('PRE', 'verdadeiro', proximoNT="expr_rel1")
                self.expr_rel1()
            elif( self.token['PRE'] == 'falso'):
                self.match('PRE', 'falso', proximoNT="expr_rel1")
                self.expr_rel1()
            else:
                erro = "Esperado: expr_art ou 'verdadeiro' ou 'falso'"
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("expr_rel", self.token):
                return self.expr_rel()
            elif sequinte("expr_rel", self.token):
                return
            else:
                raise e
    
    def expr_rel0(self):
        try:
            if( primeiro("expr_rel") ):
                self.expr_rel()
            elif( self.token['lexema'] == '('):
                self.match('DEL', '(', proximoNT="expressao")
                self.expressao()
                self.match('DEL', ')')
            else:
                erro = "Esperado: expr_rel ou '('"
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("expr_rel0", self.token):
                return self.expr_rel0()
            elif sequinte("expr_rel0", self.token):
                return
            else:
                raise e
    
    def expr_rel1(self):
        try:
            if( primeiro("operator_rel") ):
                self.operator_rel()
                self.expr_rel0()
            else:
                return # declaracao vazia
                
        except Exception as e:
            if primeiro("expr_rel1", self.token):
                return self.expr_rel1()
            elif sequinte("expr_rel1", self.token):
                return
            else:
                raise e
    
    def operator_rel(self):
        try:
            if ( self.token['lexema'] == '=='):
                self.match('REL', '==')
            elif ( self.token['lexema'] == '>='):
                self.match('REL', '>=')
            elif ( self.token['lexema'] == '<='):
                self.match('REL', '<=')
            elif ( self.token['lexema'] == '!='):
                self.match('REL', '!=')
            elif ( self.token['lexema'] == '>'):
                self.match('REL', '>')
            elif ( self.token['lexema'] == '<'):
                self.match('REL', '!=')
            else:
                erro = "Esperado: '==', '>=', '<=', '!=', '>' ou '<'"
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("operator_rel", self.token):
                return self.operator_rel()
            elif sequinte("operator_rel", self.token):
                return
            else:
                raise e
    
    def expr_log1(self):
        try:
            if( primeiro("operatorLog") ):
                self.operatorLog()
                self.expressao()
            else:
                return # declaracao vazia
        except Exception as e:
            if primeiro("expr_log1", self.token):
                return self.expr_log1()
            elif sequinte("expr_log1", self.token):
                return
            else:
                raise e

    def expr_log2(self):
        try:
            if( primeiro("operatorLog") ):
                self.operatorLog()
                self.expressao()
            elif( primeiro("operator_multi") ):
                self.operator_multi()
                self.expressao()
            elif( primeiro("operator_rel") ):
                self.operator_rel()
                self.expressao()
            elif( primeiro("operator_soma") ):
                self.operator_soma()
                self.expressao()
            else:
                return # declaracao vazia
        except Exception as e:
            if primeiro("expr_log2", self.token):
                return self.expr_log2()
            elif sequinte("expr_log2", self.token):
                return
            else:
                raise e
    
    def operator_log(self):
        try:
            if ( self.token['lexema'] == '&&'):
                self.match('LOG', '&&')
            elif ( self.token['lexema'] == '||'):
                self.match('LOG', '||')
            else:
                erro = "Esperado: && ou ||"
                self.registrarErro(erro)
                
        except Exception as e:
            if primeiro("operator_log", self.token):
                return self.operator_log()
            elif sequinte("operator_log", self.token):
                return
            else:
                raise e