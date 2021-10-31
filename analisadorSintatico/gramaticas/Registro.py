
class Registro:
    
    def declaracao_reg(self):
        
        try:
            if( self.token['lexema'] == 'registro' ):
                self.match("PRE", "registro", proximoToken={"tipo": "IDE"})
                self.match("IDE", proximoToken={"tipo": "DEL", "lexema": "{"})
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
                    self.proximoToken()
            raise e
        
    def declaracao_reg1(self):
        
        try:
            if( primeiro("type", self.token) ):
                self.type()
                self.match("IDE", proximoNT="declaracao_reg2")
                self.declaracao_reg4()
                self.declaracao_reg2()
            else:
                erro = 'Esperado: type'
                self.registrarErro(erro)
                raise Exception('Erro sintático', erro + '; Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
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
                self.match("IDE", proximoNT="declaracao_reg2")
                self.declaracao_reg2()
            elif( self.token['lexema'] == ';' ):
                self.match("DEL", ";", proximoNT="declaracao_reg3")
                self.declaracao_reg3()
            else:
                erro = "Esperado: ',' ou ';'"
                self.registrarErro(erro)
                raise Exception('Erro sintático', erro + '; Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
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
                self.declaracao_reg()
            elif( primeiro("declaracao_reg1", self.token) ):
                self.declaracao_reg1()
            else:
                erro = "Esperado: '}' ou declaracao_reg1"
                self.registrarErro(erro)
                raise Exception('Erro sintático', erro +'; encontrados: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
            
        except Exception as e:
            if primeiro("declaracao_reg3", self.token):
                return self.declaracao_reg3()
            elif sequinte("declaracao_reg3", self.token):
                return
            else:
                raise e
            
    def declaracao_reg4(self):
        
        try:
            if( primeiro("v_m_access", self.token) ):
                self.v_m_access()
            else:
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
                self.match("DEL", ".", proximoToken={"tipo": "IDE"})
                self.match("IDE", ".", proximoNT="nested_elem_registro")
                self.nested_elem_registro()
            else:
                erro = "Esperado: '.'"
                self.registrarErro(erro)
                raise Exception('Erro sintático', erro +'; encontrados: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
            
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
                self.match("DEL", ".", proximoToken={"tipo": "IDE"})
                self.match("IDE", ".", proximoNT="nested_elem_registro1")
                self.nested_elem_registro1()
            elif( primeiro("v_m_access") ):
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
            if( primeiro("elem_registro") ):
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