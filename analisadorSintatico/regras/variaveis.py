from gramatica import *

class Variaveis:

  def __init__(self):
    pass

  def start(self):
    if(self.token['lexema'] == 'variaveis'):
      self.match("PRE", "variaveis")
      self.match("IDE")
      self.match("DEL", "{")
      self.step2()
      
  def step2(self):
    if(primeiro("type", self.token)):
        self.type()
        self.match("IDE")
        self.step3()
    else:
        raise Exception('Erro sintático', 'Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])
    
  def step3(self):
    if(self.token['lexema'] == '='):
      self.match("REL")
      if (self.match("NRO") or self.match("CAD")):
        self.step4()
      else:
        raise Exception('Erro sintático', 'Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])
    else:
      self.step4()

  def step4(self):
    if(self.token['lexema'] == ','):
      self.match("DEL", ",")
      self.match("IDE")
      self.step3()
    elif(self.token['lexema'] == ';'):
      self.match("DEL", ";")
      self.step5()
    else:
        raise Exception('Erro sintático', 'Esperado: , ou ;, Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])
  
  def step5(self):
    if(self.token['lexema'] == '}'):
        self.match("DEL", "}")
    else:
        raise Exception('Erro sintático', 'Encontrados: ' + self.token['tipo'] + ' ' + self.token['lexema'])