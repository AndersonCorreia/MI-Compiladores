import os, sys
# codigo abaixo inserer a pasta raiz no python para ser possivel acessar as outras pastas e arquivos do diretorio
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from fileHelper import *
from analisadorLexico.TokenAutomato import TokenAutomato

dir = dirname(__file__) + "/../input"
dirOutput = dirname(__file__) + "/../output"

arquivos = getArquivos(dir)

for arquivo in arquivos:
    automato = TokenAutomato(getCaminhoAbsoluto(arquivo, dir))
    automato.analisarArquivo()
    tokens = automato.getListaTokens()
    errors = automato.getListaErrors()
    fileNumber = getNumeracaoByNameFile(arquivo)
    gerarArquivosDeSaida(dirOutput, fileNumber, tokens, errors)

    for t in tokens:
        print("Lexema: " + t['lexema'] + "; " + "Tipo: " + t['tipo'] + "; " + "Linha: " + str(t['linha']))
        
    print("\n\n Erros: \n")
    
    for e in errors:
        print("erro: " + e['lexema'] + "; " + "Tipo: " + e['tipo'] + "; " + "Linha: " + str(e['linha']))

