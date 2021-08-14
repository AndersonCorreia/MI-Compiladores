from fileHelper import *


# gerarArquivosDeSaida("nome qualquer")
try:
    print( str.encode('ã', encoding='ascii').hex())
except ValueError:
    print("caractere incorreto")
    
