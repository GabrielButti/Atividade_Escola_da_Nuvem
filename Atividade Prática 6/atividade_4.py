'''4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.  '''

import requests
from datetime import datetime

def buscar_cotacao(moeda):
    """Consulta a cotação de uma moeda em relação ao Real (BRL) na API AwesomeAPI."""
    try:
        # Formata a moeda em maiúsculas
        moeda = moeda.upper()
        
        # URL da API AwesomeAPI
        url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        # Extrai a chave da moeda (ex: USDBRL, EURBRL)
        chave_moeda = f"{moeda}BRL"
        
        if chave_moeda not in dados:
            return None
        
        cotacao = dados[chave_moeda]
        
        # Converte timestamp para data/hora legível
        timestamp = int(cotacao['timestamp'])
        data_hora = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')
        
        return {
            'moeda': moeda,
            'valor_atual': float(cotacao['bid']),
            'valor_maximo': float(cotacao['high']),
            'valor_minimo': float(cotacao['low']),
            'data_hora': data_hora
        }
    
    except requests.exceptions.RequestException:
        return None
    except Exception:
        return None

# Programa principal
print("=" * 60)
print("CONSULTOR DE COTAÇÕES DE MOEDAS - AwesomeAPI")
print("=" * 60)

while True:
    print("\n1. Consultar cotação de moeda")
    print("2. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        moeda = input("\nDigite o código da moeda (ex: USD, EUR, GBP): ")
        print("\nBuscando cotação...")
        
        resultado = buscar_cotacao(moeda)
        
        if resultado:
            print("\n" + "=" * 60)
            print(f"COTAÇÃO DE {resultado['moeda']} EM RELAÇÃO AO REAL (BRL)")
            print("=" * 60)
            print(f"Valor atual: R$ {resultado['valor_atual']:.4f}")
            print(f"Valor máximo: R$ {resultado['valor_maximo']:.4f}")
            print(f"Valor mínimo: R$ {resultado['valor_minimo']:.4f}")
            print(f"Data/Hora da atualização: {resultado['data_hora']}")
            print("=" * 60)
        else:
            print("\n❌ Erro na consulta!")
            print("Moeda não encontrada ou erro na conexão.")
            print("Verifique o código da moeda e tente novamente.")
            print("Exemplos: USD, EUR, GBP, JPY, CAD, AUD, CHF")
    
    elif opcao == '2':
        print("\nAté logo!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")