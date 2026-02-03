'''Crie um programa que cria um arquivo CSV com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. '''


import csv

def criar_csv(caminho_arquivo):
    # Dados das pessoas
    pessoas = [
        ["Nome", "Idade", "Cidade"],
        ["Ana", 28, "São Paulo"],
        ["Bruno", 34, "Rio de Janeiro"],
        ["Carla", 22, "Belo Horizonte"],
        ["Diego", 40, "Curitiba"]
    ]

    try:
        # Abre (ou cria) o arquivo CSV
        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(pessoas)

        print(f"Arquivo '{caminho_arquivo}' salvo com sucesso!")

    except Exception as e:
        print(f"Falha ao salvar o arquivo CSV: {e}")


# Programa principal
nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")
criar_csv(nome_arquivo)
