from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Variaveis:
  
  def declaration_var(self):
    try:
      self.semanticoHelper['variavel'] = {}
      self.semanticoHelper['variavel']['escopo'] = self.semanticoHelper['escopo']
      if(self.token['lexema'] == 'variaveis'):
        self.match("PRE", "variaveis", proximoToken={"tipo": "DEL", "lexema": "{"})
        self.match("DEL", "{", proximoNT="declaration_var1")
        self.declaration_var1()
      else:
        erro = 'Tokens e Não-Terminais Esperados: variaveis'
        self.registrarErro(erro)
    except Exception as e:
      # while self.token['tipo'] != 'EOF':
      #   if primeiro("declaration_var", self.token):
      #       return self.declaration_var()
      #   elif sequinte("declaration_var", self.token):
      #       return
      #   else:
      #     self.tokensIgnorados.append(self.token)
      #     self.proximoToken()
      raise e

  def declaration_var1(self):
    try:
      self.semanticoHelper['variavel']['init'] = False
      if(primeiro("type", self.token)):
        self.salvarTokenTemp = True
        self.type()
        self.semanticoHelper['variavel']['tipo'] = self.tokenTemp['lexema']
        self.match("IDE", proximoNT="declaration_var2")
        self.semanticoHelper['variavel']['nomeToken'] = self.tokenTemp
        self.semanticoHelper['tokenIDE'] = self.tokenTemp
        self.salvarTokenTemp = False
        self.declaration_var2()
      elif( self.token['lexema'] == '}' ):
        self.match("DEL", "}")
      else:
        erro = 'Tokens e Não-Terminais Esperados: type ou }'
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
      self.semanticoHelper['variavel']['categoria'] = None
      if(self.token['lexema'] == '=' ):
          self.match("REL", "=", proximoNT="value")
          self.semanticoHelper['variavel']['init'] = True
          self.salvarTokenTemp = True
          self.value()
          self.semanticoHelper['variavel']['valueToken'] = self.tokenTemp
          self.salvarTokenTemp = False
          self.semanticoHelper['variavel']['categoria'] = 'variavel'
          self.declaration_var3()
      elif(primeiro("vector_matrix", self.token)):
          self.vector_matrix()
      elif(primeiro("declaration_var3", self.token)):
          self.semanticoHelper['variavel']['categoria'] = 'variavel'
          self.declaration_var3()
      else:
          erro = "Tokens ou Não-Terminais Esperados: =, vector_matrix ou declaration_var3"
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
          if not self.tabelaDeSimbolos.addVariables(self.semanticoHelper['variavel']['nomeToken'], self.semanticoHelper['variavel']):
            self.registrarErrosSemanticos()
          self.salvarTokenTemp = True
          self.match("IDE", proximoNT="declaration_var2")
          self.semanticoHelper['tokenIDE'] = self.tokenTemp
          self.semanticoHelper['variavel']['nomeToken'] = self.tokenTemp
          self.semanticoHelper['variavel']['init'] = False
          self.salvarTokenTemp = False
          self.declaration_var2()
      elif(self.token['lexema'] == ';' ):
          self.match("DEL", ";", proximoNT="declaration_var1")
          if not self.tabelaDeSimbolos.addVariables(self.semanticoHelper['variavel']['nomeToken'], self.semanticoHelper['variavel']):
            self.registrarErrosSemanticos()
          self.declaration_var1()
      else:
          erro = "Tokens ou Não-Terminais Esperados: ',' ou ';'"
          self.registrarErro(erro)
    except Exception as e:
      if primeiro("declaration_var3", self.token):
          return self.declaration_var3()
      elif sequinte("declaration_var3", self.token):
          return
      else:
          raise e