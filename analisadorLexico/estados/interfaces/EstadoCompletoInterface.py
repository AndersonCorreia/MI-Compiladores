from analisadorLexico.estados.interfaces.EstadoInterface import EstadoInterface

class EstadoCompletoInterface(EstadoInterface):
    
    def lexemaCompleto(self):
        return True
    
    def isError(self):
        return False