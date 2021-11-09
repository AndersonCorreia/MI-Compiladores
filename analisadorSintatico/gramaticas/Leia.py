from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Leia:
  
  def read_cmd(self):
    try:
      if(self.token['lexema'] == 'leia'):
        self.match("PRE", "leia", proximoToken={"tipo": "DEL", "lexema": "("})
        self.match("DEL", "(", proximoNT="read_value")
        self.read_value()
        self.read_value_list()
        self.match("DEL", ")", proximoToken={"tipo": "DEL", "lexema": ";"})
        self.match("DEL", ";")
      else:
        erro = "Tokens ou Não-Terminais Esperados: escreva"
        self.registrarErro(erro)
    except Exception as e:
        if primeiro("write_cmd", self.token):
            return self.write_cmd()
        elif sequinte("write_cmd", self.token):
            return
        else:
            raise e

  def read_value_list(self):
    try:
      if(self.token['lexema'] == ',' ):
          self.match("DEL", ",", proximoNT="read_value")
          self.read_value()
          self.read_value_list()
      else:
          return # declaração vazia
    except Exception as e:
      if primeiro("read_value_list", self.token):
          return self.read_value_list()
      elif sequinte("read_value_list", self.token):
          return
      else:
          raise e