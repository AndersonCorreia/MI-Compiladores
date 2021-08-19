

class EstadoInterface:
    """
    Classe que representa a interface para o conjunto de estados do analisador léxico.
    """

    @staticmethod
    def getProximoEstado(char, lexema):
        """
        Método que retorna o próximo estado do automato a partir do caractere e do lexema até então.
        :param char: Caractere a ser analisado.
        :param lexema: Lexema a ser analisado.
        :return: O próximo estado do automato.
        """
        raise NotImplementedError("Método não implementado")
    
    @staticmethod
    def caractereCompoemLexema():
        """
        Método que informa se o ultimo caractere lido faz parte do lexema
        :return: True se encontrado, False caso contrário.
        """
        raise NotImplementedError("Método não implementado")
    
    @staticmethod
    def lexemaCompleto():
        """
        Método que retorna se o lexema esta completo
        :return: True se encontrado, False caso contrário.
        """
        raise NotImplementedError("Método não implementado")
    
    @staticmethod
    def isError():
        """
        Método que retorna se o estado é um estado de erro
        :return: True se for um erro, False caso contrário.
        """
        raise NotImplementedError("Método não implementado")
    
    @staticmethod
    def getTipo():
        """
        Método que retorna o tipo do token ou do erro
        :return: string que indentifica o tipo do token ou do erro
        """
        raise NotImplementedError("Método não implementado")
    
    @staticmethod
    def getSigla():
        """
        Método que retorna a sigla do token ou do erro
        :return: string sigla que indentifica o tipo do token ou do erro
        """
        raise NotImplementedError("Método não implementado")
    
    @staticmethod
    def getMetadados():
        """
        Método que retorna os metadados possiveis de se indentificar deste token
        :return: dict com os metadados do estado
        """
        return {}
    
    @staticmethod
    def finalDoArquivo():
        """
        Método para retornar o estado caso chegue ao final do arquivo
        :return: EstadoInterface
        """
        raise NotImplementedError("Método não implementado")