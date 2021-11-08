#lista dos primeiros de Não-Terminal definidos apenas pelo tipo e valores. 
# Se o array de valores esta vazio, o primeiro é qualquer token daquele tipo
primeiros = {
    "primitive_type": { 'PRE': ['inteiro', 'real', 'booleano', 'char', 'cadeia', 'vazio']},
    "type": { 'IDE': []},
    "declaracao_reg": { 'PRE': ['registro']},
    "declaracao_reg2": { 'DEL': [',', ';']},
    "declaracao_reg3": { 'DEL': ['}']},
    "declaration_const": { 'PRE': ['constantes']},
    "declaration_const2": { 'DEL': [',', ';', '}']},
    "declaration_var": { 'PRE': ['variaveis']},
    "declaration_var2": { 'DEL': [';'], 'REL': ['=']},
    "declaration_var3": { 'DEL': [',', ';']},
    "elem_registro": { "DEL": ['.'] },
    "nested_elem_registro": { "DEL": ['.'] },
    "v_m_access": { 'DEL' : ['[']},
    "v_m_access1": { 'DEL' : ['[']},
    "expr_valor_mod": { 'NRO': []},
    "operator_soma": { 'ART': ['+', '-']},
    "operator_multi": { 'ART': ['*', '/']},
    "operator_auto0": { 'ART': ['++', '--']},
    "operator_auto": { 'ART': ['++', '--']},
    "operator_rel" : { 'REL': ['<', '>', '<=', '>=', '==', '!=']},
    "operator_log" : { 'LOG': ['&&', '||']},
    "expr_number": { 'IDE': ['(']},
    "expr_rel": { "PRE": ["verdadeiro", "falso"]},
    "expressao": { "DEL": ["(",], "LOG": ["!"]},
    "read_value": { 'IDE': []},
    "se": { 'PRE': ['se']},
    "senao": { 'PRE': ['senao']},
    "com_retornar": { 'PRE': ['retorno']},
    "com_enquanto": { 'PRE': ['enquanto']},
    "com_para": { 'PRE': ['para']},
    "value": { 'NRO': [], 'PRE': ["verdadeiro", "falso"], 'CAD': [], 'CAR': [] },
    "write_value_list": { 'DEL': [','] },
    "value_with_expressao": { 'CAD': [], 'CAR': [] },
    "functionCall": { 'IDE': []},
    "function_declaration": { 'PRE': ['funcao']},
    "function_declaration1": { 'PRE': ['algoritmo']},
    "function_declaration2": { 'IDE': []},
    "function_parameters1": { 'PRE': [] },
    "function_parameters2": { 'DEL' : ['['] },
    "function_parameters3": { 'DEL' : ['['] },
    "function_parameters4": { 'DEL': [','] }
}

NT_contem_palavra_vazia = [ 
    "declaracao_reg", "declaracao_reg4", "nested_elem_registro", "v_m_access1",
    "expr_multi_pos", "expr_art1", "operator_auto", "com_body", "com_retornar", 
    "com_retornar1"
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

    if NT == "value":
        if primeiro("value", token, considerar_palavra_vazia):
            return True
    if NT == "declaration_const1":
        if primeiro("type", token, considerar_palavra_vazia):
            return True
    if NT == "declaration_var1":
        if primeiro("type", token, considerar_palavra_vazia):
            return True
    if NT == "declaracao_reg1":
        if primeiro("type", token, considerar_palavra_vazia):
            return True
    if NT == "declaracao_reg3":
        if primeiro("declaracao_reg1", token, considerar_palavra_vazia):
            return True
    elif NT == "declaracao_reg4":
        if primeiro("v_m_access", token, considerar_palavra_vazia):
            return True
    elif NT == "type":
        if primeiro("primitive_type", token, considerar_palavra_vazia):
            return True
    elif NT == "nested_elem_registro":
        if primeiro("v_m_access", token, considerar_palavra_vazia):
            return True
    elif NT == "expr_valor_mod":
        if primeiro("operator_auto0", token, considerar_palavra_vazia) or primeiro("read_value", token, considerar_palavra_vazia):
            return True
    elif NT == "expr_multi":
        if primeiro("operator_soma", token, considerar_palavra_vazia) or primeiro("expr_valor_mod", token, considerar_palavra_vazia):
            return True
    elif NT == "expr_art":
        if primeiro("expr_multi", token, considerar_palavra_vazia):
            return True
    elif NT == "expr_multi_pos":
        if primeiro("operator_multi", token, considerar_palavra_vazia):
            return True
    elif NT == "expr_art1":
        if primeiro("operator_soma", token, considerar_palavra_vazia):
            return True
    elif NT == "expr_number":
        if primeiro("expr_art", token, considerar_palavra_vazia):
            return True
    elif NT == "expr_rel":
        if primeiro("expr_art", token, considerar_palavra_vazia):
            return True
    elif NT == "expressao":
        if primeiro("expr_rel", token, considerar_palavra_vazia):
            return True
    elif NT == "var_atr":
        if primeiro("read_value", token, considerar_palavra_vazia):
            return True
    elif NT in ["stop", "value_with_expressao"]:
        if primeiro("expressao", token, considerar_palavra_vazia):
            return True
    elif NT == "com_body":
        if primeiro("com_enquanto", token, considerar_palavra_vazia) or primeiro("com_para", token, considerar_palavra_vazia) or primeiro("se", token, considerar_palavra_vazia) or primeiro("com_retornar", token, considerar_palavra_vazia) or primeiro("write_cmd", token, considerar_palavra_vazia) or primeiro("read_cmd", token, considerar_palavra_vazia) or primeiro("functionCall", token, considerar_palavra_vazia) or primeiro("var_atr", token, considerar_palavra_vazia):
            return True
    
    if NT in primeiros:
        if token['tipo'] in primeiros[NT]:
            if primeiros[NT][token['tipo']] == [] or token['lexema'] in primeiros[NT][token['tipo']]:
                return True
    if NT in NT_contem_palavra_vazia and considerar_palavra_vazia:
        return True
        
    return False

def primeiro_sem_palavra_vazia(NT, token):
    return primeiro(NT, token, considerar_palavra_vazia=False) 

sequintes = {
    "primitive_type": { 'IDE': []},
    "type": { 'IDE': []},
    "v_m_access": { 'DEL' : ['[']},
    "expressao": { "DEL": [")", ";", ","]},
    "stop": {"DEL": [';']},
    "com_body": { "DEL": ['}']},
    "com_retornar1": { "DEL": [';']},
    "args": { "DEL": [')']},
    "functionCall": { "DEL": [';',',']},
}

def sequinte(NT, token):
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
        if sequinte("declaracao_reg4", token) or primeiro_sem_palavra_vazia("nested_elem_registro1", token) or sequinte("nested_elem_registro", token) or sequinte("read_value0", token):
            return True
    elif NT == "v_m_access1": 
        if sequinte("v_m_access", token):
            return True
    elif NT == "type": 
        if primeiro_sem_palavra_vazia("function_declaration1", token):
            return True
    elif NT == "declaracao_reg": 
        if primeiro_sem_palavra_vazia("declaration_const", token):
            return True
    elif NT == "declaracao_reg4": 
        if primeiro_sem_palavra_vazia("declaracao_reg2", token):
            return True
    elif NT == "expr_art": 
        if primeiro_sem_palavra_vazia("expr_rel1", token) or sequinte('expr_rel', token):
            return True
    elif NT == "expr_number": 
        if sequinte("expr_art", token):
            return True
    elif NT == "expr_rel": 
        if primeiro_sem_palavra_vazia("expr_log1", token) or sequinte("expressao", token):
            return True
    elif NT in ["expr_rel1", "expr_rel0"]: 
        if sequinte("expr_rel", token):
            return True
    elif NT in ["expr_log1", "expr_log2"]: 
        if sequinte("expressao", token):
            return True
    elif NT == "expressao": 
        if sequinte("value_with_expressao", token):
            #sequinte de outros terminais são ')' e ';' que já estão na lista de sequinte
            # mantendo o value_with_expressao por segurança já que o mais usado
            return True
    elif NT in ["se", "com_enquanto", "com_para", "write_cmd", "read_cmd", "functionCall"]:
        if primeiro_sem_palavra_vazia("function_body2", token) or primeiro_sem_palavra_vazia("com_body", token):
            return True
    elif NT == "var_atr":
        if primeiro_sem_palavra_vazia("function_body2", token) or primeiro_sem_palavra_vazia("com_body", token) or sequinte("init", token):
            return True
    elif NT == "init":
        if primeiro_sem_palavra_vazia("stop", token):
            return True
    elif NT in ["senao", "se_senao", "se_body"]:
        if sequinte("se", token):
            return True
    elif NT == "com_retornar":
        if sequinte("com_body", token):
            return True
    
    if NT in sequintes:
        if token['tipo'] in sequintes[NT]:
            if sequintes[NT][token['tipo']] == [] or token['lexema'] in sequintes[NT][token['tipo']]:
                return True
    
    return False
    