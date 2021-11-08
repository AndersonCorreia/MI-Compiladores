from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Constantes:
  
  def declaration_const(self):
    try:
      if(self.token['lexema'] == 'constantes'):
        self.match("PRE", "constantes", proximoToken={"tipo": "DEL", "lexema": "{"})
        self.match("DEL", "{", proximoNT="declaration_const1")
        self.declaration_const1()
      else:
        return
    except Exception as e:
      while self.token['tipo'] != 'EOF':
        if primeiro("declaration_const", self.token):
            return self.declaration_const()
        elif sequinte("declaration_const", self.token):
            return
        else:
          self.tokensIgnorados.append(self.token)
          self.proximoToken()
      raise e

  def declaration_const1(self):
    try:
      if(primeiro("primitive_type", self.token)):
        self.type()
        self.match("IDE", proximoToken={"tipo": "REL", "lexema": "="})
        self.match("REL", "=", proximoNT="value")
        self.value()
        self.declaration_const2()
      elif(self.token['lexema'] == '}' ):
        self.match("DEL", "}")
      else:
        erro = 'Esperado: primitive_type ou }'
        self.registrarErro(erro)
    except Exception as e:
      if primeiro("declaracao_const1", self.token):
        return self.declaration_const1()
      elif sequinte("declaracao_const1", self.token):
          return
      else:
          raise e
      
  def declaration_const2(self):
    try:
      if(self.token['lexema'] == ',' ):
          self.match("DEL", ",", proximoToken={"tipo": "IDE"})
          self.match("IDE", proximoNT="value")
          self.value()
          self.declaration_const2()
      elif(self.token['lexema'] == ';' ):
          self.match("DEL", ";", proximoNT="declaration_const1")
          self.declaration_const1()
      else:
          erro = "Tokens ou Não-Terminais Esperados: ',' ou ';'"
          self.registrarErro(erro)
    except Exception as e:
      if primeiro("declaration_const2", self.token):
          return self.declaration_const2()
      elif sequinte("declaration_const2", self.token):
          return
      else:
          raise e