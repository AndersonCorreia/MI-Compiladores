from functools import reduce

class SymbolTable:
    
    def __init__(self):
        self.functionsTable = {}
        self.structsTable = {}
        self.varConstTable = {}
        self.erros = []
        
    # retornar todos os erros e limpa o array de erros, chamar apenas no momento de gravar os erros semanticos no analisador
    def getErros(self):
        erros = self.erros
        self.erros = []
        return erros
    
    def addErro(self, token, msg):
        erro = {'token': token, 'erro': msg }
        self.erros.append(erro)

    def functionExists(self, functionNameToken, functionParameters = [], returnIfExists = False):
        key = self._getFunctionKey(functionNameToken, functionParameters)
        if key in self.functionsTable:
            return self.functionsTable[key] if returnIfExists else True
        return False
    
    def addFunction(self, functionNameToken, functionParameters = [], returnType = "vazio"):
        if self.functionExists(functionNameToken, functionParameters):
            erro = { 'token': functionNameToken, 'erro': 'A função ' + functionNameToken['lexema'] + ' já foi declarada com estes parâmetros.' }
            self.erros.append(erro)
            return False
        self._insertFunction(functionNameToken, returnType, functionParameters)
        return True
    
    def callFunction(self, functionNameToken, functionParameters = []):
        if not self.functionExists(functionNameToken, functionParameters):
            functionsSameName = self.getFunctionsByName(functionNameToken['lexema'])
            if( len(functionsSameName) == 0):
                erroMsg = 'Não existe nenhuma função com o nome \'' + functionNameToken['lexema'] + '\''
            else:
                erroMsg = 'Não existe uma função \'' + functionNameToken['lexema'] + '\' com esta lista de parametros.\n As funções existentes:\n'
                for func in functionsSameName:
                    erroMsg += '\t' + func['nome'] + '(' + ','.join(map(lambda x: x, func['parametros'])) + ')\n'
            erro = {'token': functionNameToken, 'erro': erroMsg }
            self.erros.append(erro)
            return False
        return True
    
    def getFunctionsByName(self, functionName):
        return list(
            filter(lambda x: x["nome"] == functionName, self.functionsTable.values())
        )
        
    def deleteVarsAndConstsEscopoLocal(self):
        dicionario = self.varConstTable
        lista = filter(lambda x: x["escopo"] == 'global', dicionario.values() )
        self.varConstTable = {}
        for item in lista:
            self.varConstTable[item['nome']] = item
        
    def _insertFunction(self, functionNameToken, functionReturn, functionParameters = []):
        key = self._getFunctionKey(functionNameToken, functionParameters)
        self.functionsTable[key] = {
            "nome" : functionNameToken['lexema'],
            "retorno" : functionReturn,
            "qtdParametros" :  len(functionParameters),
            "parametros": functionParameters
        }
        
        
    def _getFunctionKey(self, functionNameToken, functionParameters = []):
        qtdParameters = len(functionParameters)
        if qtdParameters > 0:
            parametrosStr = reduce(lambda x, y: str(x) + str(y), functionParameters)
        else:
            parametrosStr = ""
        key = functionNameToken['lexema'] + str(qtdParameters) + parametrosStr
        return key
    
    def structExists(self, key, returnIfExists = False):
        if key in self.structsTable:
            return self.structsTable[key] if returnIfExists else True
        return False
    
    def addStruct(self, structsNameToken, structFields = []):
        key = structsNameToken['lexema']
        if self.structExists(key):
            erro = { 'token': structsNameToken, 'erro': 'O registro ' + key + ' já foi declarado.' }
            self.erros.append(erro)
            return False
        self._insertStruct(key, structFields)
        return True
        
    def _insertStruct(self, key, structFields = []):
        fields = {}
        for field in structFields:
            name = field['nomeToken']['lexema']
            if name in fields:
                erro = { 'token': field['nomeToken'], 'erro': 'O campo \'' + name + '\' já foi declarado neste registro ('+key+').' }
                self.erros.append(erro)
            else:
                fields[name] = {
                    "nome": name,
                    "tipo": field['tipo'],
                    "categoria": field['categoria']
                }
        self.structsTable[key] = {
            "nome" : key,
            "atributos" : fields,
        }
    
    def getTipoByToken(self, token):
        if token['tipo'] == 'NRO':
            if float(token['lexema']) % 1 == 0:
                return 'inteiro'
            return 'real'
        if token['tipo'] == 'CAD':
            return 'cadeia'
        if token['tipo'] == 'CAR':
            return 'char'
        if token['tipo'] == 'PRE':
            if token['lexema'] == 'verdadeiro' or token['lexema'] == 'falso':
                return 'booleano'
        return token['tipo']
        

    def checkValue(self, token, tipo):
        value = token['lexema']
        if (tipo == 'inteiro' and not self.is_int(value) ):
            # erro = { 'token': token, 'erro': 'Tipo inteiro inválido.' }
            # self.erros.append(erro)
            return False

        if (tipo == 'real' and not self.is_float(value) ):
            # erro = { 'token': token, 'erro': 'Tipo real inválido.' }
            # self.erros.append(erro)
            return False

        if (tipo == 'booleano' and not (value == "verdadeiro" or value == "falso") ):
            # erro = { 'token': token, 'erro': 'Tipo booleano inválido.' }
            # self.erros.append(erro)
            return False 

        if (tipo == 'char' and (not len(value) == 1) or not isinstance(value, str  )):
            # erro = { 'token': token, 'erro': 'Tipo char inválido.' }
            # self.erros.append(erro)
            return False 

        if (tipo == 'cadeia' and not isinstance(value, str  )):
            # erro = { 'token': token, 'erro': 'Tipo cadeia inválido.' }
            # self.erros.append(erro)
            return False 
        return True
    
    def varOrConstExists(self, key, returnIfExists = False):
        if key in self.varConstTable:
            return self.varConstTable[key] if returnIfExists else True
        return False

    def addVariables(self, varNameToken, var = {}):
        key = varNameToken['lexema']
        
        if self.varOrConstExists(key):
            erro = { 'token': varNameToken, 'erro': 'A variável/constante ' + key + ' já foi declarada.' }
            self.erros.append(erro)
            return False
        if 'valueToken' in var:
            if not self.checkValue(var['valueToken'], var['tipo']):
                erro = { 'token': var['valueToken'], 'erro': 'Valor incorreto para a variavel do tipo ' + var['tipo'] }
                self.erros.append(erro)
                return False
            
        variavel = {
            "nome": key,
            "tipo": var['tipo'],
            "categoria": var['categoria'],
            "escopo": var['escopo'],
            "dimensao": '',
            "init": var['init']
        }
        self.varConstTable[key] = variavel
        return True

    def addConstants(self, constNameToken, const = {}):
        key = constNameToken['lexema']
        
        if self.varOrConstExists(key):
            erro = { 'token': constNameToken, 'erro': 'A variável/constante ' + key + ' já foi declarada.' }
            self.erros.append(erro)
            return False
        
        if not self.checkValue(const['valueToken'], const['tipo']):
            erro = { 'token': const['valueToken'], 'erro': 'Valor incorreto para a constante do tipo ' + const['tipo'] }
            self.erros.append(erro)
            return False
            
        constante = {
            "nome": key,
            "tipo": const['tipo'],
            "categoria": 'constante',
            "escopo": const['escopo'],
            "dimensao": '',
            "init": True
        }
        self.varConstTable[key] = constante
        return True    

    def is_int(self, n):
        try:
            int(n)
            return True
        except ValueError as e:
            return False
        
    def is_float(self, n):
        try:
            float(n)
            return True
        except ValueError as e:
            return False
