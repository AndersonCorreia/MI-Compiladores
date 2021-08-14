from estados.interfaces.EstadoInterface import EstadoInterface

class EstadoCompletoInterface(EstadoInterface):
    
    @staticmethod
    def lexemaCompleto():
        return True
    
    @staticmethod
    def isErro():
        return False