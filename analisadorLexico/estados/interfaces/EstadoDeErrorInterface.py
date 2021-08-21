from estados.interfaces.EstadoInterface import EstadoInterface

class EstadoDeErrorInterface(EstadoInterface):
    
    def lexemaCompleto(self):
        return False
    
    def isError(self):
        return True