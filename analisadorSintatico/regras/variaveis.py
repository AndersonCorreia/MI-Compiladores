from gramatica import *

class Variaveis:

  def start(self):
    if( self.token['lexema'] == 'variaveis' ):
      self.match("PRE", "variaveis")
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
    if( self.token['lexema'] == ','):
        self.match("DEL", ",")
        self.match("IDE")
        self.step3()
    elif(self.token['lexema'] == ';'):
        self.match("DEL", ";")
        self.step4()
    else:
        raise Exception('Erro sintático', 'Esperado: , ou ;, Encontrado: ' + self.token['tipo'] + ' ' + self.token['lexema'])

  def step4(self):
    if( self.token['lexema'] == '}' ):
        self.match("DEL", "}")
        self.start()
    else:
        raise Exception('Erro sintático', 'Encontrados: ' + self.token['tipo'] + ' ' + self.token['lexema'])