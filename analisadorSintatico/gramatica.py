#lista dos proximos de Não-Terminal definidos apenas pelo tipo e valores. 
# Se o array de valores esta vazio, o proximo é qualquer token daquele tipo
proximos = {
    "primitive_type": { 'PRE': ['inteiro', 'real', 'booleano', 'char', 'cadeia', 'vazio']},
}

def proximo(NT, token):
    if NT in proximos:
        if token['tipo'] in proximos[NT]:
            if proximos[NT][token['tipo']] == [] or token['lexema'] in proximos[NT][token['tipo']]:
                return True
        
    return False
    