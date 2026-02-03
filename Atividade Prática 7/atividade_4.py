'''Crie um programa que leia e escreva arquivos no formato JSON, que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha. '''

import json

def salvar_json(caminho_arquivo):
    dados = {
        "nome": "Ana",
        "idade": 28,
        "cidade": "São Paulo"
    }

    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso no arquivo JSON.")

    except Exception as e:
        print(f"Falha ao salvar o arquivo JSON: {e}")


def ler_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        print("Dados lidos do arquivo JSON:")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

    except FileNotFoundError:
        print("Falha: o arquivo JSON não foi encontrado.")
    except json.JSONDecodeError:
        print("Falha: erro ao interpretar o conteúdo do arquivo JSON.")
    except Exception as e:
        print(f"Falha ao ler o arquivo JSON: {e}")


# Programa principal
nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ")

salvar_json(nome_arquivo)
ler_json(nome_arquivo)
