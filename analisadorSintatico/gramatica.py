#lista dos proximos de Não-Terminal definidos apenas pelo tipo e valores. 
# Se o array de valores esta vazio, o proximo é qualquer token daquele tipo
proximos = {
    "primitive_type": { 'PRE': ['inteiro', 'real', 'booleano', 'char', 'cadeia', 'vazio']},
    "type": { 'IDE': []},
    "declaracao_reg": { 'PRE': ['registro']},
}

def proximo(NT, token):
    if NT == "declaracao_reg1":
        #se o proximo do NT for o proximo de outro NT
        return proximo("type", token)
    elif NT == "type" and proximo("primitive_type", token):
        #se o proximo do NT for o proximo de outro NT ou algum Terminal que é verificado no final
        return True
    elif NT in proximos:
        if token['tipo'] in proximos[NT]:
            if proximos[NT][token['tipo']] == [] or token['lexema'] in proximos[NT][token['tipo']]:
                return True
        
    return False
    