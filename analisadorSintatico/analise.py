import os, sys
# codigo abaixo inserer a pasta raiz no python para ser possivel acessar as outras pastas e arquivos do diretorio
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from fileHelper import *
from analisadorLexico.TokenAutomato import TokenAutomato
from analisadorSintatico.AnalisadorSintatico import AnalisadorSintatico

dir = dirname(__file__) + "/../input"
dirOutput = dirname(__file__) + "/../output"

arquivos = getArquivos(dir)

for arquivo in arquivos:
    print ( "\nArquivo: "+ arquivo + "\n")
    automato = TokenAutomato(getCaminhoAbsoluto(arquivo, dir))
    automato.analisarArquivo()
    tokens = automato.getListaTokens()
    analisadorSintatico = AnalisadorSintatico(tokens)
    analisadorSintatico.analisarSintaxe()
    # exit(0)
