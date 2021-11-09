from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Escreva:
  
  def write_cmd(self):
    try:
      if(self.token['lexema'] == 'escreva'):
        self.match("PRE", "escreva", proximoToken={"tipo": "DEL", "lexema": "("})
        self.match("DEL", "(", proximoNT="value_with_expressao")
        self.value_with_expressao()
        self.write_value_list()
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

  def write_value_list(self):
    try:
      if(self.token['lexema'] == ',' ):
          self.match("IDE", ",", proximoNT="value_with_expressao")
          self.value_with_expressao()
          self.write_value_list()
      else:
        return
    except Exception as e:
      if primeiro("write_value_list", self.token):
          return self.write_value_list()
      elif sequinte("write_value_list", self.token):
          return
      else:
          raise e