from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Leia:
  
  def read_cmd(self):
    try:
      if(self.token['lexema'] == 'leia'):
        self.match("PRE", "leia", proximoToken={"tipo": "DEL", "lexema": "("})
        self.match("DEL", "(", proximoNT="read_value")
        self.read_value()
        self.match("DEL", proximoNT="read_value_list")
        self.read_value_list()
        self.match("DEL", ")", proximoToken={"tipo": "DEL", "lexema": ";"})
        self.match("DEL", ";")
      else:
        erro = "Tokens ou Não-Terminais Esperados: escreva"
        self.registrarErro(erro)
    except Exception as e:
      while self.token['tipo'] != 'EOF':
        if primeiro("write_cmd", self.token):
            return self.write_cmd()
        elif sequinte("write_cmd", self.token):
            return
        else:
            self.proximoToken()
      raise e

  def read_value_list(self):
    try:
      if(self.token['lexema'] == ',' ):
          self.match("IDE", ",", proximoNT="read_value")
          self.read_value()
          self.read_value_list()
      else:
          erro = "Tokens ou Não-Terminais Esperados: ','"
          self.registrarErro(erro)
    except Exception as e:
      if primeiro("read_value_list", self.token):
          return self.read_value_list()
      elif sequinte("read_value_list", self.token):
          return
      else:
          raise e

  def read_value(self):
    try:
      if(primeiro("type", self.token)):
        self.type()
        self.match("IDE", proximoNT="read_value0")
        self.read_value0()
    except Exception as e:
      if primeiro("read_value", self.token):
          return self.read_value()
      elif sequinte("read_value", self.token):
          return
      else:
          raise e

  def read_value0(self):
    try:
      if primeiro("v_m_access"):
        self.v_m_access()
      elif primeiro("elem_registro"):
        self.elem_registro()
      else:
        return
    except Exception as e:
      if primeiro("read_value0", self.token):
          return self.read_value0()
      elif sequinte("read_value0", self.token):
          return
      else:
          raise e