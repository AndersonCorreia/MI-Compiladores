import os, sys
# codigo abaixo inserer a pasta raiz no python para ser possivel acessar as outras pastas e arquivos do diretorio
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from fileHelper import *
from TokenAutomato import *

arquivos = getArquivos()

for arquivo in arquivos:
    automato = TokenAutomato(getCaminhoAbsoluto(arquivo))
    automato.analisarArquivo()
