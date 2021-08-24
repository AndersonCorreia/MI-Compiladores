import os, sys
# codigo abaixo inserer a pasta raiz no python para ser possivel acessar as outras pastas e arquivos do diretorio
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from fileHelper import *
from analisadorLexico.TokenAutomato import TokenAutomato

arquivos = getArquivos()

for arquivo in arquivos:
    automato = TokenAutomato(getCaminhoAbsoluto(arquivo))
    automato.analisarArquivo()
    tokens = automato.getListaTokens()
    for t in tokens:
        print("Lexema: " + t['lexema'] + "; " + "Tipo: " + t['tipo'] + "; " + "Linha: " + str(t['linha']))
        
    print("\n\n Erros: \n")
    
    errors = automato.getListaErrors()
    for e in errors:
        print("erro: " + e['lexema'] + "; " + "Tipo: " + e['tipo'] + "; " + "Linha: " + str(e['linha']))

