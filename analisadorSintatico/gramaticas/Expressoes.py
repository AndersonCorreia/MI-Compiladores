from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Expressoes:
    
    def expressao(self):
        try:
            if ( self.semanticoHelper['expressaoTypeReturn']  == ''):
                    self.semanticoHelper['expressaoTypeReturn'] = 'inteiro'
            self.semanticoHelper['expressaoParcialType'] = 'aritmetica'
            self.semanticoHelper['expressaoParentesesType'] = 'aritmetica'
            if( primeiro("expr_rel", self.token) ):
                self.expr_rel()
                self.expr_log1()
            elif( self.token['lexema'] == '('):
                self.match('DEL', '(', proximoNT="expressao")
                self.semanticoHelper['expressaoParentesesType'] = 'aritmetica'
                self.expressao()
                self.semanticoHelper['expressaoParcialType'] = self.semanticoHelper['expressaoParentesesType']
                self.match('DEL', ')')
                self.expr_log2()
            elif( self.token['lexema'] == '!'):
                self.match('DEL', '!', proximoNT="expressao")
                self.expressao()
                if(self.semanticoHelper['expressaoTypeReturn'] != 'booleano'):
                    self.tabelaDeSimbolos.addErro( self.tokenTemp, "Negação só pode ser usada em um booleano")
                    self.registrarErrosSemanticos()
                self.semanticoHelper['expressaoTypeReturn'] = 'booleano'
            else:
                erro = "Tokens ou Não-Terminais Esperados: expr_rel ou '(' ou '!'"
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
            if ( primeiro("expr_multi", self.token) ):
                self.expr_multi()
                self.expr_art1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: expr_multi"
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
            if ( primeiro("operator_soma", self.token) ):
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
                self.semanticoHelper['expressaoEsperandoValor'] = False
                if ( self.semanticoHelper['expressaoParcialType'] != 'aritmetica' ):
                    self.tabelaDeSimbolos.addErro( self.token, "Um operador aritmetico só pode ser usado com operandos inteiros ou reais")
                    self.registrarErrosSemanticos()
                self.match('ART', '+')
            elif ( self.token['lexema'] == '-'):
                self.semanticoHelper['expressaoEsperandoValor'] = False
                if ( self.semanticoHelper['expressaoParcialType'] != 'aritmetica' ):
                    self.tabelaDeSimbolos.addErro( self.token, "Um operador aritmetico só pode ser usado com operandos inteiros ou reais")
                    self.registrarErrosSemanticos()
                self.match('ART', '-')
            else:
                erro = "Tokens ou Não-Terminais Esperados: + ou -"
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
                self.semanticoHelper['expressaoEsperandoValor'] = False
                if ( self.semanticoHelper['expressaoParcialType'] != 'aritmetica' ):
                    self.tabelaDeSimbolos.addErro( self.token, "Um operador aritmetico só pode ser usado com operandos inteiros ou reais")
                    self.registrarErrosSemanticos()
                self.match('ART', '*')
            elif ( self.token['lexema'] == '/'):
                self.semanticoHelper['expressaoEsperandoValor'] = False
                if ( self.semanticoHelper['expressaoParcialType'] != 'aritmetica' ):
                    self.tabelaDeSimbolos.addErro( self.token, "Um operador aritmetico só pode ser usado com operandos inteiros ou reais")
                    self.registrarErrosSemanticos()
                self.match('ART', '/')
            else:
                erro = "Tokens ou Não-Terminais Esperados: * ou /"
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
                self.semanticoHelper['expressaoEsperandoValor'] = False
                self.match('ART', '++')
            elif ( self.token['lexema'] == '--'):
                self.semanticoHelper['expressaoEsperandoValor'] = False
                self.match('ART', '--')
            else:
                erro = "Tokens ou Não-Terminais Esperados: ++ ou --"
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
                self.semanticoHelper['expressaoEsperandoValor'] = False
                if ( self.semanticoHelper['expressaoParcialType'] != 'aritmetica' ):
                    self.tabelaDeSimbolos.addErro( self.token, "Um operador aritmetico só pode ser usado com operandos inteiros ou reais")
                    self.registrarErrosSemanticos()
                self.match('ART', '++')
            elif ( self.token['lexema'] == '--'):
                self.semanticoHelper['expressaoEsperandoValor'] = False
                if ( self.semanticoHelper['expressaoParcialType'] != 'aritmetica' ):
                    self.tabelaDeSimbolos.addErro( self.token, "Um operador aritmetico só pode ser usado com operandos inteiros ou reais")
                    self.registrarErrosSemanticos()
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
            self.semanticoHelper['expressaoParcialType'] = 'aritmetica'
            if ( self.token['tipo'] == "NRO"):
                self.salvarTokenTemp = True
                self.match("NRO")
                tipo = self.tabelaDeSimbolos.getTipoByToken(self.tokenTemp)
                if ( self.semanticoHelper['expressaoTypeReturn']  == 'inteiro' and tipo == 'real'):
                    self.semanticoHelper['expressaoTypeReturn'] = 'real' 
                    # se a expressão como um todo ainda é aritimetica(sem comparações), agora ira retornar um real
            elif ( primeiro("operator_auto0", self.token) ):
                self.operator_auto0()
                self.read_value() # falta verificar o tipo do identificador
                key = self.semanticoHelper['tokenIDE']['lexema']
                if key in self.tabelaDeSimbolos.varConstTable:
                    tipo = self.tabelaDeSimbolos.varConstTable[key]['tipo']
                    if tipo == 'real':
                        if ( self.semanticoHelper['expressaoTypeReturn']  == 'inteiro'):
                            self.semanticoHelper['expressaoTypeReturn'] = 'real' 
                    elif tipo == 'booleano':
                        self.semanticoHelper['expressaoParcialType'] = 'logico_relacional'
                        if ( self.semanticoHelper['expressaoTypeReturn']  == 'inteiro' or self.semanticoHelper['expressaoTypeReturn']  == 'real'):
                            self.semanticoHelper['expressaoTypeReturn'] = 'logico_relacional'
                    elif self.semanticoHelper['expressaoEsperandoValor'] == False:
                        self.tabelaDeSimbolos.addErro( self.semanticoHelper['tokenIDE'], "Numa expressão só é permitido identificadores do tipo inteiro, real ou booleano")
                        self.registrarErrosSemanticos()
            elif ( primeiro("read_value", self.token) ):
                self.read_value() # falta verificar o tipo do identificador
                key = self.semanticoHelper['tokenIDE']['lexema']
                if key in self.tabelaDeSimbolos.varConstTable:
                    tipo = self.tabelaDeSimbolos.varConstTable[key]['tipo']
                    if tipo == 'real':
                        if ( self.semanticoHelper['expressaoTypeReturn']  == 'inteiro'):
                            self.semanticoHelper['expressaoTypeReturn'] = 'real' 
                    elif tipo == 'booleano':
                        self.semanticoHelper['expressaoParcialType'] = 'logico_relacional'
                        if ( self.semanticoHelper['expressaoTypeReturn']  == 'inteiro' or self.semanticoHelper['expressaoTypeReturn']  == 'real'):
                            self.semanticoHelper['expressaoTypeReturn'] = 'logico_relacional'
                    elif self.semanticoHelper['expressaoEsperandoValor'] == False and tipo != 'inteiro':
                        self.tabelaDeSimbolos.addErro( self.semanticoHelper['tokenIDE'], "Numa expressão só é permitido identificadores do tipo inteiro, real ou booleano")
                        self.registrarErrosSemanticos() 
                self.operator_auto()
            else:
                erro = "Tokens ou Não-Terminais Esperados: NRO, operator_auto0 ou read_value"
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
            if ( primeiro("operator_soma", self.token) ):
                self.operator_soma()
                self.expr_valor_mod()
                self.expr_multi_pos()
            elif ( primeiro("expr_valor_mod", self.token) ):
                self.expr_valor_mod()
                self.expr_multi_pos()
            else:
                erro = "Tokens ou Não-Terminais Esperados: operator_soma, expr_valor_mod"
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
            if ( primeiro("operator_multi", self.token) ):
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
            if ( self.semanticoHelper['expressaoTypeReturn']  == ''):
                    self.semanticoHelper['expressaoTypeReturn'] = 'inteiro' 
            if( primeiro("expr_art", self.token) ):
                self.expr_art()
            elif( self.token['lexema'] == '('):
                self.match('DEL', '(', proximoNT="expr_number")
                self.expr_number()
                self.match('DEL', '(', proximoNT="expr_multi_pos")
                self.expr_multi_pos()
                self.expr_number1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: expr_art ou '('"
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
            if( primeiro("operator_soma", self.token) ):
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
            if( primeiro("expr_art", self.token) ):
                self.expr_art()
                self.expr_rel1()
            elif( self.token['lexema'] == 'verdadeiro'):
                self.match('PRE', 'verdadeiro', proximoNT="expr_rel1")
                self.semanticoHelper['expressaoParentesesType'] = 'logico_relacional'
                self.semanticoHelper['expressaoTypeReturn'] = 'booleano'
                self.expr_rel1()
            elif( self.token['lexema'] == 'falso'):
                self.semanticoHelper['expressaoParentesesType'] = 'logico_relacional'
                self.semanticoHelper['expressaoTypeReturn'] = 'booleano'
                self.match('PRE', 'falso', proximoNT="expr_rel1")
                self.expr_rel1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: expr_art ou 'verdadeiro' ou 'falso'"
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
            if( primeiro("expr_rel", self.token) ):
                self.expr_rel()
            elif( self.token['lexema'] == '('):
                self.match('DEL', '(', proximoNT="expressao")
                self.semanticoHelper['expressaoParentesesType'] = 'aritmetica'
                self.expressao()
                self.semanticoHelper['expressaoParcialType'] = self.semanticoHelper['expressaoParentesesType']
                self.match('DEL', ')')
            else:
                erro = "Tokens ou Não-Terminais Esperados: expr_rel ou '('"
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
            if( primeiro("operator_rel", self.token) ):
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
            self.semanticoHelper['expressaoEsperandoValor'] = False
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
                self.match('REL', '<')
            else:
                erro = "Tokens ou Não-Terminais Esperados: '==', '>=', '<=', '!=', '>' ou '<'"
                self.registrarErro(erro)
            
            self.semanticoHelper['expressaoParentesesType'] = 'logico_relacional'
            self.semanticoHelper['expressaoTypeReturn'] = 'booleano'
        except Exception as e:
            if primeiro("operator_rel", self.token):
                return self.operator_rel()
            elif sequinte("operator_rel", self.token):
                return
            else:
                raise e
    
    def expr_log1(self):
        try:
            if( primeiro("operator_log", self.token) ):
                self.operator_log()
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
            if( primeiro("operator_log", self.token) ):
                self.operator_log()
                self.expressao()
            elif( primeiro("operator_multi", self.token) ):
                self.operator_multi()
                self.expressao()
            elif( primeiro("operator_rel", self.token) ):
                self.operator_rel()
                self.expressao()
            elif( primeiro("operator_soma", self.token) ):
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
                self.semanticoHelper['expressaoEsperandoValor'] = False
                self.match('LOG', '&&')
            elif ( self.token['lexema'] == '||'):
                self.semanticoHelper['expressaoEsperandoValor'] = False
                self.match('LOG', '||')
            else:
                erro = "Tokens ou Não-Terminais Esperados: && ou ||"
                self.registrarErro(erro)
            
            self.semanticoHelper['expressaoTypeReturn'] = 'booleano'
            self.semanticoHelper['expressaoParentesesType'] = 'logico_relacional'
        except Exception as e:
            if primeiro("operator_log", self.token):
                return self.operator_log()
            elif sequinte("operator_log", self.token):
                return
            else:
                raise e