from estados.interfaces.EstadoInterface import EstadoInterface

class EstadoAbertoInterface(EstadoInterface):
    
    @staticmethod
    def lexemaCompleto():
        return False
    
    @staticmethod
    def isErro():
        return False
    
    @staticmethod
    def getTipo():
        return "token incompleto"