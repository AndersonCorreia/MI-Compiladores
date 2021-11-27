from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Registro:
    
    def declaracao_reg(self):
        
        try:
            self.semanticoHelper['structNomeToken'] = None
            self.semanticoHelper['structFields'] = []
            if( self.token['lexema'] == 'registro' ):
                self.match("PRE", "registro", proximoToken={"tipo": "IDE"})
                self.salvarTokenTemp = True
                self.match("IDE", proximoToken={"tipo": "DEL", "lexema": "{"})
                self.semanticoHelper['structNomeToken'] = self.tokenTemp
                self.salvarTokenTemp = False
                self.match("DEL", "{", proximoNT="declaracao_reg1")
                self.declaracao_reg1()
            else:
                return # declaração vazia
        except Exception as e:
            while self.token['tipo'] != 'EOF':
                if primeiro("declaracao_reg", self.token):
                    return self.declaracao_reg()
                elif sequinte("declaracao_reg", self.token):
                    return
                else:
                    self.tokensIgnorados.append(self.token)
                    self.proximoToken()
            raise e
        
    def declaracao_reg1(self):
        
        try:
            self.semanticoHelper['structFieldTemp'] = {}
            if( primeiro("type", self.token) ):
                self.salvarTokenTemp = True
                self.type()
                self.semanticoHelper['structFieldTemp']['tipo'] = self.tokenTemp['lexema']
                self.match("IDE", proximoNT="declaracao_reg4")
                self.semanticoHelper['structFieldTemp']['nomeToken'] = self.tokenTemp
                self.salvarTokenTemp = False
                self.declaracao_reg4()
                self.semanticoHelper['structFields'].append(self.semanticoHelper['structFieldTemp'])
                self.declaracao_reg2()
            else:
                erro = 'Tokens e Não-Terminais Esperados: type'
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("declaracao_reg1", self.token):
                return self.declaracao_reg1()
            elif sequinte("declaracao_reg1", self.token):
                return
            else:
                raise e
         
    def declaracao_reg2(self):
        
        try:
            if( self.token['lexema'] == ',' ):
                self.match("DEL", ",", proximoToken={"tipo": "IDE"})
                tipo = self.semanticoHelper['structFieldTemp']['tipo']
                self.semanticoHelper['structFieldTemp'] = {}
                self.semanticoHelper['structFieldTemp']['tipo'] = tipo
                self.salvarTokenTemp = True
                self.match("IDE", proximoNT="declaracao_reg4")
                self.semanticoHelper['structFieldTemp']['nomeToken'] = self.tokenTemp
                self.salvarTokenTemp = False
                self.declaracao_reg4()
                self.semanticoHelper['structFields'].append(self.semanticoHelper['structFieldTemp'])
                self.declaracao_reg2()
            elif( self.token['lexema'] == ';' ):
                self.match("DEL", ";", proximoNT="declaracao_reg3")
                self.declaracao_reg3()
            else:
                erro = "Tokens ou Não-Terminais Esperados: ',' ou ';'"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("declaracao_reg2", self.token):
                return self.declaracao_reg2()
            elif sequinte("declaracao_reg2", self.token):
                return
            else:
                raise e
        
    def declaracao_reg3(self):
        
        try:
            if( self.token['lexema'] == '}' ):
                self.match("DEL", "}", proximoNT="declaracao_reg")
                if not self.tabelaDeSimbolos.addStruct(self.semanticoHelper['structNomeToken'], self.semanticoHelper['structFields']):
                    self.registrarErrosSemanticos()
                self.declaracao_reg()
            elif( primeiro("declaracao_reg1", self.token) ):
                self.declaracao_reg1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: '}' ou declaracao_reg1"
                self.registrarErro(erro)
            
        except Exception as e:
            if primeiro("declaracao_reg3", self.token):
                return self.declaracao_reg3()
            elif sequinte("declaracao_reg3", self.token):
                return
            else:
                raise e
            
    def declaracao_reg4(self):
        
        try:
            self.semanticoHelper['structFieldTemp']['categoria'] = None
            if( primeiro("v_m_access", self.token) ):
                self.v_m_access()
                self.semanticoHelper['structFieldTemp']['categoria'] = self.semanticoHelper['v_m_access']['tipo']
            else:
                self.semanticoHelper['structFieldTemp']['categoria'] = 'variavel'
                return # declaração vazia
            
        except Exception as e:
            if primeiro("declaracao_reg4", self.token):
                return self.declaracao_reg4()
            elif sequinte("declaracao_reg4", self.token):
                return
            else:
                raise e

    def elem_registro(self):
        
        try:
            if( self.token['lexema'] == '.' ):
                self.match("DEL", ".")
                self.salvarTokenTemp = True
                self.match("IDE", proximoNT="nested_elem_registro")
                self.semanticoHelper['tokenIDE'] = self.tokenTemp
                self.salvarTokenTemp = False
                self.nested_elem_registro()
            else:
                erro = "Tokens ou Não-Terminais Esperados: '.'"
                self.registrarErro(erro)
            
        except Exception as e:
            if primeiro("elem_registro", self.token):
                return self.elem_registro()
            elif sequinte("elem_registro", self.token):
                return
            else:
                raise e
    
    def nested_elem_registro(self):
        
        try:
            if( self.token['lexema'] == '.' ):
                self.match("DEL", ".")
                self.match("IDE", proximoNT="nested_elem_registro1")
                self.nested_elem_registro1()
            elif( primeiro("v_m_access", self.token) ):
                self.v_m_access()
                self.nested_elem_registro1()
            else:
                return # declaração vazia
            
        except Exception as e:
            if primeiro("nested_elem_registro", self.token):
                return self.nested_elem_registro()
            elif sequinte("nested_elem_registro", self.token):
                return
            else:
                raise e
            
    def nested_elem_registro1(self):
        
        try:
            if( primeiro("elem_registro", self.token) ):
                self.elem_registro()
            else:
                return # declaração vazia
            
        except Exception as e:
            # if primeiro("nested_elem_registro1", self.token):
            #     return self.nested_elem_registro1()
            # elif sequinte("nested_elem_registro1", self.token):
            #     return
            # else:
            #     raise e
            # simplificando esse NT especifico pode apenas lançar o erro
            raise e