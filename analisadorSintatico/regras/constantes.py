from gramatica import *

class Constantes:

  def start(self):
    if(self.token['lexema'] == 'constantes'):
      self.match("PRE", "constantes")
      self.match("IDE")
      self.match("DEL", "{")
      self.step2()
      
  def step2(self):
    if(proximo("type", self.token)):
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
      raise Exception('Erro sintático', 'Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])

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