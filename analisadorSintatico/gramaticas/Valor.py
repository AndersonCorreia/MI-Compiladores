from analisadorSintatico.gramaticaHelper import primeiro, sequinte
class Valor:

    def value(self):
        try:
            if self.token['tipo'] == 'NRO':
                self.match("NRO")
            elif self.token['lexema'] == 'verdadeiro':
                self.match("PRE", "verdadeiro")
            elif self.token['lexema'] == 'falso':
                self.match("PRE", "falso")
            elif self.token['tipo'] == 'CAD':
                self.match("CAD")
            elif self.token['tipo'] == 'CAR':
                self.match("CAR")
            else:
                erro = "Tokens e Não-Terminais Esperados: NRO, 'verdadeiro', 'falso', CAD, CAR"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("value", self.token):
                return self.value()
            elif sequinte("value", self.token):
                return
            else:
                raise e

    def value_with_IDE(self):
        try:
            if primeiro("value", self.token):
                self.value()
            elif self.token['tipo'] == 'IDE':
                self.match("IDE")
            else:
                erro = "Tokens e Não-Terminais Esperados: value, IDE"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("value_with_IDE", self.token):
                return self.value_with_IDE()
            elif sequinte("value_with_IDE", self.token):
                return
            else:
                raise e

    def value_with_expressao(self):
        try:
            if primeiro("expressao", self.token):
                self.semanticoHelper['expressaoTypeReturn']  = '' #importante: reseta o tipo de retorno da expressao
                self.semanticoHelper['expressaoEsperandoValor']  = True
                self.expressao()
            elif self.token['tipo'] == 'CAD':
                self.match("CAD")
            elif self.token['tipo'] == 'CAR':
                self.match("CAR")
            else:
                erro = "Tokens e Não-Terminais Esperados: expressao, CAD, CAR"
                self.registrarErro(erro)
        except Exception as e:
            if primeiro("value_with_expressao", self.token):
                return self.value_with_expressao()
            elif sequinte("value_with_expressao", self.token):
                return
            else:
                raise e