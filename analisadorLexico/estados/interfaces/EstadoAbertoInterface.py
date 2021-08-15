from estados.interfaces.EstadoInterface import EstadoInterface

class EstadoAbertoInterface(EstadoInterface):
    
    @staticmethod
    def lexemaCompleto():
        return False
    
    @staticmethod
    def isError():
        return False
    
    @staticmethod
    def getTipo():
        return "token incompleto"