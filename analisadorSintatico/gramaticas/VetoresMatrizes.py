
class VetoresMatrizes:
    
        
    def v_m_access(self):
        try:
            # if( primeiro("v_m_access", self.token) ):
            #     self.v_m_access()
            # else:
            #     return # declaração vazia
            return
            
        except Exception as e:
            if primeiro("v_m_access", self.token):
                return self.v_m_access()
            elif sequinte("v_m_access", self.token):
                return
            else:
                raise e