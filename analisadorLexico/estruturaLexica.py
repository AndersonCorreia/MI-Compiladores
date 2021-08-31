delimitadores = [' ', ';', '(', ')', '{', '}', '[', ']', '.', '\n', '\t']
delimitadorSemToken = ['\n','\t', ' '] # lista de caracteres que funcionam como delimitadores mas não são tokens e devem ser ignorados
simbolosPermitidos = [ hex(32) , hex(126) ]# intervalo fechado de valores hexadecimais dos simbolos permitidos
simbolosPermitidosOutros = [ hex(25) ]# valores hexadecimais de outros simbolos permitidos, 25 = %
simbolosExcecoes = [ hex(34), hex(39) ]# valores hexadecimais no intervalo que não são simbolos permitidos
operadoresAritimetricos = ['+', '-', '*', '/', '++', '--']
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
        return simbolosPermitidos[0] <= charHex <= simbolosPermitidos[1] and charHex not in simbolosExcecoes or isDelimitador(char) or charHex in simbolosPermitidosOutros
    except: # se o simbolo não estiver na tabela ascii ocorre um erro
        return False
    
def isDigito(char):
    return char.isdigit()
    
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


def isOperadorLogico(lexema):
    return lexema in operadoresLogicos

def maybeOperadorLogico(lexema):
    for operador in operadoresLogicos:
        if operador.startswith(lexema):
            return True
    return False

def isOperadorAritimetrico(lexema):
    return lexema in operadoresAritimetricos

def maybeOperadorAritimetrico(lexema):
    for operador in operadoresAritimetricos:
        if operador.startswith(lexema):
            return True
    return False

def isOperadorRelacional(lexema):
    return lexema in operadoresRelacionais

def maybeOperadorRelacional(lexema):
    for operador in operadoresRelacionais:
        if operador.startswith(lexema):
            return True
    return False

def maybeComentarioBloco(lexema):
    if lexema == "{":
        return True
    return False