from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Variaveis:
  
  def declaration_var(self):
    try:
      if(self.token['lexema'] == 'variaveis'):
        self.match("PRE", "variaveis", proximoToken={"tipo": "DEL", "lexema": "{"})
        self.match("DEL", "{", proximoNT="declaration_var1")
        self.declaration_var1()
      else:
        erro = 'Esperado: variaveis'
        self.registrarErro(erro)
    except Exception as e:
      while self.token['tipo'] != 'EOF':
        if primeiro("declaration_var", self.token):
            return self.declaration_var()
        elif sequinte("declaration_var", self.token):
            return
        else:
          self.tokensIgnorados.append(self.token)
          self.proximoToken()
      raise e

  def declaration_var1(self):
    try:
      if(primeiro("type", self.token)):
        self.type()
        self.match("IDE", proximoNT="declaration_var2")
        self.declaration_var2()
      elif( self.token['lexema'] == '}' ):
        self.match("DEL", "}")
      else:
        erro = 'Esperado: type ou }'
        self.registrarErro(erro)
    except Exception as e:
      if primeiro("declaration_var1", self.token):
        return self.declaration_var1()
      elif sequinte("declaration_var1", self.token):
          return
      else:
          raise e
      
  def declaration_var2(self):
    try:
      if(self.token['lexema'] == '=' ):
          self.match("REL", "=", proximoNT="value")
          self.value()
          self.declaration_var3()
      elif( primeiro("vector_matrix", self.token) ):
          self.vector_matrix()
      elif( primeiro("declaration_var3", self.token) ):
          self.declaration_var3()
      else:
          erro = "Esperado: =, vector_matrix ou declaration_var3"
          self.registrarErro(erro)
    except Exception as e:
      if primeiro("declaration_const2", self.token):
          return self.declaration_var2()
      elif sequinte("declaration_const2", self.token):
          return
      else:
          raise e

  def declaration_var3(self):
    try:
      if(self.token['lexema'] == ',' ):
          self.match("DEL", ",", proximoToken={"tipo": "IDE"})
          self.match("IDE", proximoNT="declaration_var2")
          self.declaration_var2()
      elif(self.token['lexema'] == ';' ):
          self.match("DEL", ";", proximoNT="declaration_var1")
          self.declaration_var1()
      else:
          erro = "Esperado: ',' ou ';'"
          self.registrarErro(erro)
    except Exception as e:
      if primeiro("declaration_var3", self.token):
          return self.declaration_var3()
      elif sequinte("declaration_var3", self.token):
          return
      else:
          raise e