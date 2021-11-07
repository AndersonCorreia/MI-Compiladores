from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Constantes:
  
  def declaration_const(self):
    if(self.token['lexema'] == 'constantes'):
      self.match("PRE", "constantes")
      self.match("IDE")
      self.match("DEL", "{")
      self.declaration_const1()
      
  def declaration_const1(self):
    if(primeiro("primitive_type", self.token)):
        self.primitive_type()
        self.match("IDE")
        self.match("REL", "=")
        if (self.match("NRO") or self.match("CAD")):
          self.declaration_const2()
        else:
          raise Exception('Erro sintático', 'Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
    else:
        raise Exception('Erro sintático', 'Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
      
  def declaration_const2(self):
    if(self.token['lexema'] == ','):
      self.match("DEL", ",")
      self.match("IDE")
      if(self.token['lexema'] == '='):
        self.match("REL")
        if (self.match("NRO") or self.match("CAD")):
          self.declaration_const2()
        else:
          raise Exception('Erro sintático', 'Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
    elif(self.token['lexema'] == ';'):
      self.match("DEL", ";")
      self.step5()
    else:
        raise Exception('Erro sintático', 'Esperado: , ou ;, Encontrado: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")
  
  def step5(self):
    if(self.token['lexema'] == '}'):
        self.match("DEL", "}")
    else:
        raise Exception('Erro sintático', 'Encontrados: ' + self.token['tipo'] + " '" + self.token['lexema'] + "'")