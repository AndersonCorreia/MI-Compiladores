from analisadorLexico.estados.interfaces.EstadoInterface import EstadoInterface

class EstadoAbertoInterface(EstadoInterface):
    
    def lexemaCompleto(self):
        return False
    
    def isError(self):
        return False
    
    def getTipo(self):
        return "token incompleto"