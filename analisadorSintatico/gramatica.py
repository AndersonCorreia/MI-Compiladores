#lista dos primeiros de Não-Terminal definidos apenas pelo tipo e valores. 
# Se o array de valores esta vazio, o primeiro é qualquer token daquele tipo
# o tipo & representa a palavra vazia
primeiros = {
    "primitive_type": { 'PRE': ['inteiro', 'real', 'booleano', 'char', 'cadeia', 'vazio']},
    "type": { 'IDE': []},
    "declaracao_reg": { 'PRE': ['registro'], '&': []},
}

sequintes = {
}

def primeiro(NT, token):
    if NT == "declaracao_reg1":
        #se o primeiro do NT for o primeiro de outro NT
        return primeiro("type", token)
    elif NT == "type" and primeiro("primitive_type", token):
        #se o primeiro do NT for o primeiro de outro NT ou algum Terminal que é verificado no final
        return True
    elif NT in primeiros:
        if token['tipo'] in primeiros[NT]:
            if primeiros[NT][token['tipo']] == [] or token['lexema'] in primeiros[NT][token['tipo']]:
                return True
        if '&' in primeiros[NT]:
            return True
        
    return False
    
def sequinte(NT, token):
    return False