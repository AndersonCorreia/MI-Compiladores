from functools import reduce

class SymbolTable:
    
    def __init__(self):
        self.functionsTable = {}
        self.structsTable = {}
        self.erros = []
        
    # retornar todos os erros e limpa o array de erros, chamar apenas no momento de gravar os erros semanticos no analisador
    def getErros(self):
        erros = self.erros
        self.erros = []
        return erros

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
    
    def getFunctionsByName(self, functionNameToken):
        return list(
            filter(lambda x: x["nome"] == functionNameToken, self.functionsTable.values())
        )
        
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
    
        