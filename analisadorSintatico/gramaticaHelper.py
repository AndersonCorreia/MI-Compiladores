#lista dos primeiros de Não-Terminal definidos apenas pelo tipo e valores. 
# Se o array de valores esta vazio, o primeiro é qualquer token daquele tipo
primeiros = {
    "primitive_type": { 'PRE': ['inteiro', 'real', 'booleano', 'char', 'cadeia', 'vazio']},
    "type": { 'IDE': []},
    "declaracao_reg": { 'PRE': ['registro']},
    "declaracao_reg2": { 'DEL': [',', ';']},
    "declaracao_reg3": { 'DEL': ['}']},
    "declaration_const": { 'PRE': ['constantes']},
    "elem_registro": { "DEL": ['.'] },
    "nested_elem_registro": { "DEL": ['.'] },
    "v_m_access": { 'DEL' : ['[']},
    "v_m_access1": { 'DEL' : ['[']},
}

NT_contem_palavra_vazia = [ 
    "declaracao_reg", "declaracao_reg4", "nested_elem_registro", "v_m_access1"
]

def primeiro(NT, token, considerar_palavra_vazia=True):
    # exemplos de como estruturar os ifs:
    # if NT == "declaracao_reg1":
    #     #se o primeiro do NT for o primeiro de outro NT
    #     return primeiro("type", token)
    # elif NT == "type":
    #     if primeiro("primitive_type", token):
    #         #se o primeiro do NT for o primeiro de outro NT ou algum Terminal que é verificado no final
    #         return True
    
    if NT == "declaracao_reg1":
        if primeiro("type", token):
            return True
    if NT == "declaracao_reg3":
        if primeiro("declaracao_reg1", token):
            return True
    elif NT == "declaracao_reg4":
        if primeiro("v_m_access", token):
            return True
    elif NT == "type":
        if primeiro("primitive_type", token):
            return True
    elif NT == "nested_elem_registro":
        if primeiro("v_m_access", token):
            return True
    
    if NT in primeiros:
        if token['tipo'] in primeiros[NT]:
            if primeiros[NT][token['tipo']] == [] or token['lexema'] in primeiros[NT][token['tipo']]:
                return True
    if NT in NT_contem_palavra_vazia and considerar_palavra_vazia:
        return True
        
    return False
 
 

sequintes = {
    "primitive_type": { 'IDE': []},
    "type": { 'IDE': []},
    "v_m_access": { 'DEL' : ['[']},
}
   
def sequinte(NT, token):
    considerar_palavra_vazia = False
    if NT == "primitive_type": 
        if sequinte("type", token):
            return True
    if NT == "elem_registro": 
        if sequinte("read_value", token):
            return True
    if NT == "nested_elem_registro": 
        if sequinte("elem_registro", token):
            return True
    elif NT == "v_m_access": 
        if sequinte("declaracao_reg4", token) or primeiro("nested_elem_registro1", token, considerar_palavra_vazia) or sequinte("nested_elem_registro", token) or sequinte("read_value0", token):
            return True
    elif NT == "v_m_access1": 
        if sequinte("v_m_access", token):
            return True
    elif NT == "type": 
        if primeiro("function_declaration1", token):
            return True
    elif NT == "declaracao_reg": 
        if primeiro("declaration_const", token):
            return True
    elif NT == "declaracao_reg4": 
        if primeiro("declaracao_reg2", token):
            return True
    
    if NT in sequintes:
        if token['tipo'] in sequintes[NT]:
            if sequintes[NT][token['tipo']] == [] or token['lexema'] in sequintes[NT][token['tipo']]:
                return True
        
    return False
    