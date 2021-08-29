from estruturaLexica import *
class EstadoInterface:
    """
    Classe que representa a interface para o conjunto de estados do analisador léxico.
    """

    def __init__(self, automato):
        self.automato = automato
    
    def getProximoEstado(self, char, lexema):
        """
        Método que retorna o próximo estado do automato a partir do caractere e do lexema até então.
        :param char: Caractere a ser analisado.
        :param lexema: Lexema a ser analisado.
        :return: O próximo estado do automato.
        """
        raise NotImplementedError("Método não implementado")
    
    def caractereCompoemLexema(self):
        """
        Método que informa se o ultimo caractere lido faz parte do lexema
        :return: True se encontrado, False caso contrário.
        """
        raise NotImplementedError("Método não implementado")
    
    def lexemaCompleto(self):
        """
        Método que retorna se o lexema esta completo
        :return: True se encontrado, False caso contrário.
        """
        raise NotImplementedError("Método não implementado")
    
    def isError(self):
        """
        Método que retorna se o estado é um estado de erro
        :return: True se for um erro, False caso contrário.
        """
        print(self)
        raise NotImplementedError("Método não implementado")
    
    def getTipo(self):
        """
        Método que retorna o tipo do token ou do erro
        :return: string que indentifica o tipo do token ou do erro
        """
        print(self)
        raise NotImplementedError("Método não implementado")
    
    def getSigla(self):
        """
        Método que retorna a sigla do token ou do erro
        :return: string sigla que indentifica o tipo do token ou do erro
        """
        raise NotImplementedError("Método não implementado")
    
    def getMetadados(self):
        """
        Método que retorna os metadados possiveis de se indentificar deste token
        :return: dict com os metadados do estado
        """
        return {}
    
    def finalDoArquivo(self, lexema):
        """
        Método para retornar o estado final caso chegue ao final do arquivo
        :return: EstadoInterface
        """
        raise NotImplementedError("Método não implementado")
    
    def isLexemaErrorCompleto(self, char, lexema):
        """
        Método para determinar quando o lexema de um erro está completo
        :return: True se o lexema de um erro está completo, False caso contrário.
        """
        raise NotImplementedError("Método não implementado")
    
    def pularDelimitadorSemToken(self):
        """
        Método para determinar se deve pular um delimitador sem token
        :return: True se deve pular, False caso contrário.
        """
        return True