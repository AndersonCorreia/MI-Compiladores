from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class VetoresMatrizes:
    
    def vector_matrix(self):
        try:
            if( self.token['lexema'] == '[' ):
                self.match( "DEL", '[', proximoNT="expr_number" )
                self.expr_number()
                self.match( "DEL", ']', proximoNT="v_m_access1" )
                self.vector_matrix_1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: '['"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("vector_matrix", self.token):
                return self.vector_matrix()
            elif sequinte("vector_matrix", self.token):
                return
            else:
                raise e
    
    def vector_matrix_1(self):
        try:
            if(self.token['lexema'] == '[' ):
                self.match( "DEL", '[', proximoNT="expr_number" )
                self.expr_number()
                self.match( "DEL", ']', proximoNT="vector_matrix_2" )
                self.vector_matrix_2()
            elif(self.token['lexema'] == '=' ):
                self.match( "REL", '=', proximoNT="init_vector" )
                self.init_vector()
                self.declaration_var3()
            elif primeiro("declaration_var3", self.token):
                self.declaration_var3()
            else:
                erro = "Tokens ou Não-Terminais Esperados: '[', '=' ou declaration_var3"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("vector_matrix_1", self.token):
                return self.vector_matrix_1()
            elif sequinte("vector_matrix_1", self.token):
                return
            else:
                raise e

    def vector_matrix_2(self):
        try:
            if(self.token['lexema'] == '=' ):
                self.match( "REL", '=', proximoNT="init_matrix" )
                self.init_matrix()
                self.declaration_var3()
            elif primeiro("declaration_var3", self.token):
                self.declaration_var3()
            else:
                erro = "Tokens ou Não-Terminais Esperados: lexema '[' ou '="
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("vector_matrix_2", self.token):
                return self.vector_matrix_2()
            elif sequinte("vector_matrix_2", self.token):
                return
            else:
                raise e
        
    def init_matrix(self):
        try:
            if(self.token['lexema'] == '[' ):
                self.match( "DEL", '[', proximoNT="init_matrix_1" )
                self.init_matrix_1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: '[' ou init_matrix_1"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("init_matrix", self.token):
                return self.init_matrix()
            elif sequinte("init_matrix", self.token):
                return
            else:
                raise e

    def init_matrix_1(self):
        try:
            if(primeiro("value_with_IDE", self.token)):
                self.value_with_IDE()
                self.init_matrix_2()
            else:
                erro = "Tokens ou Não-Terminais Esperados: valor com identificador"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("init_matrix_1", self.token):
                return self.init_matrix_1()
            elif sequinte("init_matrix_1", self.token):
                return
            else:
                raise e

    def init_matrix_2(self):
        try:
            if(self.token['lexema'] == ',' ):
                self.match( "DEL", ',', proximoNT="init_matrix_1" )
                self.init_matrix_1()
            elif(self.token['lexema'] == ';' ):
                self.match( "DEL", ';', proximoNT="init_matrix_1" )
                self.init_matrix_1()
            elif(self.token['lexema'] == ']' ):
                self.match( "DEL", ']')
            else:
                erro = "Tokens ou Não-Terminais Esperados: lexema ',' ou ';' ou ']'"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("init_matrix_2", self.token):
                return self.init_matrix_2()
            elif sequinte("init_matrix_2", self.token):
                return
            else:
                raise e

    def init_vector(self):
        try:
            if(self.token['lexema'] == '[' ):
                self.match( "DEL", '[', proximoNT="init_vector_1" )
                self.init_vector_1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: lexema '['"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("init_vector", self.token):
                return self.init_vector()
            elif sequinte("init_vector", self.token):
                return
            else:
                raise e

    def init_vector_1(self):
        try:
            if(primeiro("value_with_IDE", self.token)):
                self.value_with_IDE()
                self.init_vector_2()
            else:
                erro = "Tokens ou Não-Terminais Esperados: valor com identificador"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("init_vector_1", self.token):
                return self.init_vector_1()
            elif sequinte("init_vector_1", self.token):
                return
            else:
                raise e

    def init_vector_2(self):
        try:
            if(self.token['lexema'] == ',' ):
                self.match( "DEL", ',', proximoNT="init_vector_1" )
                self.init_vector_1()
            elif(self.token['lexema'] == ']' ):
                self.match( "DEL", ']')
            else:
                erro = "Tokens ou Não-Terminais Esperados: lexema ',' ou ']'"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("init_vector_2", self.token):
                return self.init_vector_2()
            elif sequinte("init_vector_2", self.token):
                return
            else:
                raise e

    def v_m_access(self):
        try:
            if( self.token['lexema'] == '[' ):
                self.match( "DEL", '[', proximoNT="expr_number" )
                self.expr_number()
                self.match( "DEL", ']', proximoNT="v_m_access1" )
                self.semanticoHelper['v_m_access']['tipo'] = 'array'
                self.v_m_access1()
            else:
                erro = "Tokens ou Não-Terminais Esperados: lexema '['"
                self.registrarErro(erro)
            
        except Exception as e:
            if primeiro("v_m_access", self.token):
                return self.v_m_access()
            elif sequinte("v_m_access", self.token):
                return
            else:
                raise e
            
    def v_m_access1(self):
        try:
            if( self.token['lexema'] == '[' ):
                self.match( "DEL", '[', proximoNT="expr_number" )
                self.expr_number()
                self.match( "DEL", ']')
                self.semanticoHelper['v_m_access']['tipo'] = 'matriz'
            else:
                return  # declaração vazia
            
        except Exception as e:
            if primeiro("v_m_access1", self.token):
                return self.v_m_access1()
            elif sequinte("v_m_access1", self.token):
                return
            else:
                raise e