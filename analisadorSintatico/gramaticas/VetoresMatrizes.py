
class VetoresMatrizes:
    
        
    def v_m_access(self):
        try:
            if( self.token['lexema'] == '[' ):
                self.match( "DEL", '[', proximoNT="exprNumber" )
                self.exprNumber()
                self.match( "DEL", ']', proximoNT="v_m_access1" )
                self.v_m_access1()
            else:
                erro = "Esperado: lexema '['"
                self.registrarErro(erro)
            return
            
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
                self.match( "DEL", '[', proximoNT="exprNumber" )
                self.exprNumber()
                self.match( "DEL", ']')
            else:
                return  # declaração vazia
            
        except Exception as e:
            if primeiro("v_m_access1", self.token):
                return self.v_m_access1()
            elif sequinte("v_m_access1", self.token):
                return
            else:
                raise e