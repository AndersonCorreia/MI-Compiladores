delimitadores = [' ', ';', '(', ')', '{', '}', '[', ']', '.', '\n', '\t']
delimitadorSemToken = ['\n','\t', ' '] # lista de caracteres que funcionam como delimitadores mas não são tokens e devem ser ignorados
simbolosPermitidos = [ hex(32) , hex(126) ]# intervalo fechado de valores hexadecimais dos simbolos permitidos
simbolosExcecoes = [ hex(34), hex(39) ]# valores hexadecimais no intervalo que não são simbolos permitidos
operadoresAritimeticos = ['+', '-', '*', '/', '++', '--']
operadoresRelacionais = ['>', '<', '>=', '<=', '==', '!=', '=']
operadoresLogicos = [ '&&', '||', '!' ]
palavrasReservadas = [
    'algoritmo', 'variaveis', 'constantes', 'registro',
    'funcao', 'retorno', 'vazio', 'se', 'senao', 'enquanto',
    'para', 'leia', 'escreva', 'inteiro', 'real', 'booleano',
    'char', 'cadeia', 'verdadeiro', 'falso'
]

def isDelimitador(char):
    return char in delimitadores

def isDelimitadorSemToken(char):
    return char in delimitadorSemToken

def isSimboloPermitido(char):
    try:
        charHex = '0x'+bytes(char, 'ascii').hex()
        return simbolosPermitidos[0] <= charHex <= simbolosPermitidos[1] and charHex not in simbolosExcecoes or isDelimitador(char)
    except: # se o simbolo não estiver na tabela ascii ocorre um erro
        return False
    
def isDigito(char):
    try:
        charHex = bytes(char, 'ascii')
        return charHex.isnumeric()
    except: # se o simbolo não estiver na tabela ascii ocorre um erro
        return False
    
def isLetra(char):
    try:
        charHex = bytes(char, 'ascii')
        return charHex.isalpha()
    except: # se o simbolo não estiver na tabela ascii ocorre um erro
        return False
    
def isLetraDigito(char):
    try:
        charHex = bytes(char, 'ascii')
        return charHex.isalnum()
    except: # se o simbolo não estiver na tabela ascii ocorre um erro
        return False
    
def isPalavraReservada(lexema):
    return lexema in palavrasReservadas

def maybePalavraReservada(lexema):
    
    for palavra in palavrasReservadas:
        if palavra.startswith(lexema):
            return True
        
    return False