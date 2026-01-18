'''
3 - Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.'''

import requests
import re

def buscar_cep(cep):
    """Consulta informações de um CEP na API ViaCEP."""
    try:
        # Remove caracteres especiais do CEP
        cep_limpo = re.sub(r'\D', '', cep)
        
        # Valida se o CEP tem 8 dígitos
        if len(cep_limpo) != 8:
            return None
        
        # Faz a requisição à API
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        # Verifica se o CEP foi encontrado
        if 'erro' in dados:
            return None
        
        return {
            'cep': dados.get('cep', 'N/A'),
            'logradouro': dados.get('logradouro', 'N/A'),
            'bairro': dados.get('bairro', 'N/A'),
            'cidade': dados.get('localidade', 'N/A'),
            'estado': dados.get('uf', 'N/A')
        }
    
    except requests.exceptions.RequestException:
        return None
    except Exception:
        return None

# Programa principal
print("=" * 50)
print("CONSULTOR DE CEP - ViaCEP")
print("=" * 50)

while True:
    print("\n1. Consultar CEP")
    print("2. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        cep = input("\nDigite o CEP (com ou sem hífen): ")
        print("\nBuscando informações do CEP...")
        
        resultado = buscar_cep(cep)
        
        if resultado:
            print("\n" + "=" * 50)
            print("INFORMAÇÕES DO CEP")
            print("=" * 50)
            print(f"CEP: {resultado['cep']}")
            print(f"Logradouro: {resultado['logradouro']}")
            print(f"Bairro: {resultado['bairro']}")
            print(f"Cidade: {resultado['cidade']}")
            print(f"Estado: {resultado['estado']}")
            print("=" * 50)
        else:
            print("\n❌ Erro na consulta!")
            print("CEP não encontrado ou erro na conexão.")
            print("Verifique o CEP digitado e tente novamente.")
    
    elif opcao == '2':
        print("\nAté logo!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")