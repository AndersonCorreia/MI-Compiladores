from os.path import join
import os

def getArquivos(path = "./input_teste"):
    
    arquivos = []
    for arquivo in os.listdir(path):

        if arquivo.endswith(".txt") and arquivo.startswith("entrada"):
            arquivos.append(arquivo)
    return arquivos

def getNumeracaoByNameFile(arquivo):
    return arquivo.replace(".txt","").replace("entrada","")
        
def getCaminhoAbsoluto(arquivo, path = "./input_teste"):
    path = path + "/"
    return os.path.abspath(path + arquivo)

def gerarArquivosDeSaida(dirOutput, fileNumber, tokens, errors):
    with open(join(dirOutput, f'saida{fileNumber}.txt'), 'w+') as file:
        for token in tokens:
            linha = token['linha']
            tipoToken = token['tipo']
            lexema = token['lexema']
            numeroLinha = f'0{linha}' if linha <= 9 else linha
            file.write("" + str(numeroLinha) + " " + str(tipoToken) + " " + str(lexema) + "\n")
        if len(errors) > 0:
            file.write('\n')
            for error in errors:
                linha = error['linha']
                tipoErro = error['tipo']
                erroLexema = error['lexema']
                numeroLinha = f'0{linha}' if linha <= 9 else linha
                file.write("" + str(numeroLinha) + " " + str(tipoErro) + " " + str(erroLexema) + "\n")
                
def gerarArquivosDeSaidaSintatico(dirOutput, fileNumber, errors):
    with open(join(dirOutput, f'saida{fileNumber}.txt'), 'w+') as file:
        if len(errors) > 0:
            file.write('Analise concluidada\n Erros encontrados:\n')
            for error in errors:
                linha = error['linha']
                tipoErro = error['erro_sintatico']
                erroLexema = error['lexema']
                numeroLinha = f'0{linha}' if linha <= 9 else linha
                file.write("linha " + str(numeroLinha) + ": [ erro sintático: token lido \"" + str(erroLexema) + "\" ], " + str(tipoErro) + "\n")
        else:
            file.write('Analise concluidada com sucesso!\n Nenhum erro sintatico encontrado')