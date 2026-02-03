'''Crie um programa que leia um arquivo CSV informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.'''

import csv

def ler_csv(caminho_arquivo):
    try:
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
                print(linha)

    except FileNotFoundError:
        print("Erro: o arquivo CSV não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


# Programa principal
nome_arquivo = input("Digite o caminho do arquivo CSV: ")
ler_csv(nome_arquivo)
