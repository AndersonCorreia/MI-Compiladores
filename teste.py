from fileHelper import *


# gerarArquivosDeSaida("nome qualquer")
try:
    print( str.encode('%', encoding='ascii').hex())
except ValueError:
    print("caractere incorreto")
    
