from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Valor:

    def value(self):
      try:
        if primeiro("value", self.token):
          return
      except Exception as e:
        while self.token['tipo'] != 'EOF':
          if primeiro("value", self.token):
              return self.value()
          elif sequinte("value", self.token):
              return
          else:
              self.proximoToken()
        raise e

    def value_with_IDE(self):
      try:
        if primeiro("value", self.token):
          return
        elif primeiro("type", self.token):
          self.type()
      except Exception as e:
        while self.token['tipo'] != 'EOF':
          if primeiro("value_with_IDE", self.token):
              return self.value_with_IDE()
          elif sequinte("value_with_IDE", self.token):
              return
          else:
              self.proximoToken()
        raise e

    def value_with_expressao(self):
      try:
        if primeiro("expressao"):
          return
        elif primeiro("value_with_expressao"):
          return
      except Exception as e:
        while self.token['tipo'] != 'EOF':
          if primeiro("value_with_expressao", self.token):
              return self.value_with_expressao()
          elif sequinte("value_with_expressao", self.token):
              return
          else:
              self.proximoToken()
        raise e