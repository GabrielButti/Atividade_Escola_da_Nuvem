''' 2 - Crie um programa que  acesse a API Random User Generator para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.'''


import requests

def buscar_usuario_aleatorio():
    """Busca um usuário aleatório da API Random User Generator."""
    try:
        url = "https://randomuser.me/api/"
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        
        dados = resposta.json()
        usuario = dados['results'][0]
        
        # Extrai as informações necessárias
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        return {
            'nome': nome,
            'email': email,
            'pais': pais
        }
    
    except requests.exceptions.RequestException as e:
        return None

# Programa principal
print("=" * 50)
print("GERADOR DE USUÁRIOS FICTÍCIOS")
print("=" * 50)

while True:
    print("\n1. Gerar novo usuário")
    print("2. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        print("\nBuscando usuário aleatório...")
        usuario = buscar_usuario_aleatorio()
        
        if usuario:
            print("\n" + "=" * 50)
            print("USUÁRIO ALEATÓRIO")
            print("=" * 50)
            print(f"Nome: {usuario['nome']}")
            print(f"E-mail: {usuario['email']}")
            print(f"País: {usuario['pais']}")
            print("=" * 50)
        else:
            print("\n❌ Erro na conexão! Não foi possível buscar o usuário.")
            print("Verifique sua conexão com a internet e tente novamente.")
    
    elif opcao == '2':
        print("\nAté logo!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")