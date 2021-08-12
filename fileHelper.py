import os

def getArquivos(path):
    
    arquivos = []
    for arquivo in os.listdir(path):

        if arquivo.endswith(".txt") and arquivo.startswith("entrada"):
            arquivos.append(arquivo)
    return arquivos

def getNumeracaoByNameFile(arquivo):
    return arquivo.replace(".txt","").replace("entrada","")

def escreverArquivo(arquivo, texto):
    os.makedirs('output', exist_ok=True)
    with open("output/" + arquivo, "w") as f:
        f.write(texto)
 
def gerarArquivosDeSaida(text = "teste"):
    arquivos = getArquivos("./input")
    for arquivo in arquivos:
        numero = getNumeracaoByNameFile(arquivo)
        escreverArquivo("saida" + numero + ".txt", text)