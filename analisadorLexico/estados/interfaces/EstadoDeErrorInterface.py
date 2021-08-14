from estados.interfaces.EstadoInterface import EstadoInterface

class EstadoDeErrorInterface(EstadoInterface):
    
    @staticmethod
    def lexemaCompleto():
        return False
    
    @staticmethod
    def isErro():
        return True