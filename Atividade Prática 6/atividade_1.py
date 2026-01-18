'''1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.'''

import random
import string

def gerar_senha(tamanho):
    """Gera uma senha aleatória com letras, números e símbolos."""
    # Define os caracteres disponíveis
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    
    # Combina todos os caracteres
    todos_caracteres = letras + numeros + simbolos
    
    # Gera a senha aleatória
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    
    return senha

# Entrada de dados
print("=" * 50)
print("GERADOR DE SENHAS SEGURAS")
print("=" * 50)

while True:
    try:
        tamanho = int(input("\nDigite o tamanho da senha (mínimo 8): "))
        
        if tamanho < 8:
            print("A senha deve ter pelo menos 8 caracteres!")
            continue
        
        # Gera a senha
        senha_gerada = gerar_senha(tamanho)
        
        # Resultado
        print("\n" + "=" * 50)
        print(f"Sua senha segura ({tamanho} caracteres):")
        print(f"\n{senha_gerada}")
        print("=" * 50)
        
        # Pergunta se deseja gerar outra
        opcao = input("\nDeseja gerar outra senha? (S/N): ").upper()
        if opcao != 'S':
            print("\nObrigado por usar o gerador de senhas!")
            break
        
    except ValueError:
        print("Erro! Digite um número válido.")