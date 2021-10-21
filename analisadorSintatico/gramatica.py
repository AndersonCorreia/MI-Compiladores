#lista dos primeiros de Não-Terminal definidos apenas pelo tipo e valores. 
# Se o array de valores esta vazio, o primeiro é qualquer token daquele tipo
# o tipo & representa a palavra vazia
primeiros = {
    "primitive_type": { 'PRE': ['inteiro', 'real', 'booleano', 'char', 'cadeia', 'vazio']},
    "type": { 'IDE': []},
    "declaracao_reg": { 'PRE': ['registro'], '&': []},
    "declaration_const": { 'PRE': ['constantes']},
}

def primeiro(NT, token):
    if NT == "declaracao_reg1":
        #se o primeiro do NT for o primeiro de outro NT
        return primeiro("type", token)
    elif NT == "type":
        if primeiro("primitive_type", token):
            #se o primeiro do NT for o primeiro de outro NT ou algum Terminal que é verificado no final
            return True
    
    if NT in primeiros:
        if token['tipo'] in primeiros[NT]:
            if primeiros[NT][token['tipo']] == [] or token['lexema'] in primeiros[NT][token['tipo']]:
                return True
        if '&' in primeiros[NT]:
            return True
        
    return False
 
 

sequintes = {
    "primitive_type": { 'IDE': []},
    "type": { 'IDE': []},
}
   
def sequinte(NT, token):
    if NT == "primitive_type": 
        if sequinte("type", token):
            return True
    elif NT == "type": 
        if primeiro("function_declaration1", token):
            return True
    elif NT == "declaracao_reg": 
        if primeiro("declaration_const", token):
            return True
    
    if NT in sequintes:
        if token['tipo'] in sequintes[NT]:
            if sequintes[NT][token['tipo']] == [] or token['lexema'] in sequintes[NT][token['tipo']]:
                return True
        
    return False
    