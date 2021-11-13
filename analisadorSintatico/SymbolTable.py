from functools import reduce

class SymbolTable:
    
    def __init__(self):
        self.functionsTable = {}
    
    def functionExists(self, functionName, functionParameters = [], returnIfExists = False):
        key = self._getFunctionKey(functionName, functionParameters)
        if key in self.functionsTable:
            return self.functionsTable[key] if returnIfExists else True
        return False
    
    def addFunction(self, functionName, functionParameters = [], returnType = "vazio"):
        if self.functionExists(functionName, functionParameters):
            return False
        self._insertFunction(functionName, returnType, functionParameters)
        return True
    
    def getFunctionsByName(self, functionName):
        return list(
            filter(lambda x: x["nome"] == functionName, self.functionsTable.values())
        )
        
    def _insertFunction(self, functionName, functionReturn, functionParameters = []):
        key = self._getFunctionKey(functionName, functionParameters)
        self.functionsTable[key] = {
            "nome" : functionName,
            "retorno" : functionReturn,
            "qtdParametros" :  len(functionParameters),
            "parametros": functionParameters
        }
        
        
    def _getFunctionKey(self, functionName, functionParameters = []):
        qtdParameters = len(functionParameters)
        if qtdParameters > 0:
            parametrosStr = reduce(lambda x, y: str(x) + str(y), functionParameters)
        else:
            parametrosStr = ""
        key = functionName + str(qtdParameters) + parametrosStr
        return key
        