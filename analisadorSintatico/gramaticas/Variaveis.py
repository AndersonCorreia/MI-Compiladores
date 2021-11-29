from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Variaveis:
  
  def declaration_var(self):
    try:
      self.semanticoHelper['variableNomeToken'] = None
      self.semanticoHelper['blockVariables'] = []
      if(self.token['lexema'] == 'variaveis'):
        self.salvarTokenTemp = True
        self.match("PRE", "variaveis", proximoToken={"tipo": "DEL", "lexema": "{"})
        self.match("DEL", "{", proximoNT="declaration_var1")
        self.semanticoHelper['variableNomeToken'] = self.tokenTemp
        self.salvarTokenTemp = False
        self.declaration_var1()
      else:
        erro = 'Tokens e Não-Terminais Esperados: variaveis'
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
      self.semanticoHelper['variableTemp'] = {}
      self.semanticoHelper['variableTemp']['init'] = False
      self.semanticoHelper['variableTemp']['escopo'] = 'global'
      if(primeiro("type", self.token)):
        self.type()
        self.salvarTokenTemp = True
        self.match("IDE", proximoNT="declaration_var2")
        self.semanticoHelper['tokenIDE'] = self.tokenTemp
        self.semanticoHelper['variableTemp']['tipo'] = self.tokenTemp['lexema']
        self.match("IDE", proximoNT="declaration_var2")
        self.semanticoHelper['variableTemp']['nomeToken'] = self.tokenTemp
        self.salvarTokenTemp = False
        self.declaration_var2()
        self.semanticoHelper['blockVariables'].append(self.semanticoHelper['variableTemp'])
      elif( self.token['lexema'] == '}' ):
        self.match("DEL", "}")
        if not self.tabelaDeSimbolos.addVariables(self.semanticoHelper['variableNomeToken'], self.semanticoHelper['blockVariables']):
          self.registrarErrosSemanticos()
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
      self.semanticoHelper['variableTemp']['categoria'] = None
      if(self.token['lexema'] == '=' ):
          self.match("REL", "=", proximoNT="value")
          self.value()
          self.semanticoHelper['variableTemp']['init'] = True
          self.salvarTokenTemp = True
          value = self.tokenTemp['lexema']
          self.salvarTokenTemp = False
          type = self.semanticoHelper['variableTemp']['tipo']
          self.tabelaDeSimbolos.checkValue(value, type)
          self.semanticoHelper['variableTemp']['categoria'] = 'variavel'
          self.declaration_var3()
      elif(primeiro("vector_matrix", self.token)):
          self.vector_matrix()
          self.semanticoHelper['variableTemp']['categoria'] = self.semanticoHelper['vector_matrix']['tipo']
      elif(primeiro("declaration_var3", self.token)):
          self.semanticoHelper['variableTemp']['categoria'] = 'variavel'
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
          self.salvarTokenTemp = True
          tipo = self.semanticoHelper['variableTemp']['tipo']
          self.semanticoHelper['variableTemp'] = {}
          self.semanticoHelper['variableTemp']['tipo'] = tipo
          self.match("IDE", proximoNT="declaration_var2")
          self.semanticoHelper['variableTemp']['nomeToken'] = self.tokenTemp
          self.salvarTokenTemp = False
          self.semanticoHelper['blockVariables'].append(self.semanticoHelper['variableTemp'])
          self.declaration_var2()
      elif(self.token['lexema'] == ';' ):
          self.match("DEL", ";", proximoNT="declaration_var1")
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