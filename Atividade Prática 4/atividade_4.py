'''4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
'''

numeros = []
pares = 0
impares = 0

quantidade = int(input("Quantos números deseja inserir? "))

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n" + "=" * 50)
print("ANÁLISE DOS NÚMEROS")
print("=" * 50)

print(f"\nNúmeros inseridos: {numeros}")
print(f"\nTotal de números: {len(numeros)}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")

print(f"\n{'=' * 50}")