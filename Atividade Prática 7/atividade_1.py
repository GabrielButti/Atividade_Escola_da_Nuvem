'''Crie um programa que lê um arquivo CSV de logs de treinamento com a biblioteca pandas, calcule e exiba a média e o desvio padrão da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. '''


import pandas as pd

def analisar_logs(caminho_csv):
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_csv)

        # Verifica se a coluna existe
        if 'tempo_execucao' not in df.columns:
            print("Erro: a coluna 'tempo_execucao' não foi encontrada no arquivo.")
            return

        # Calcula média e desvio padrão
        media = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()

        # Exibe os resultados
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")

    except FileNotFoundError:
        print("Erro: o arquivo CSV não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: o arquivo CSV está vazio.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


# Exemplo de uso
analisar_logs("logs_treinamento.csv")
