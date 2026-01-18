'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.'''

def calcular_desconto(preco_original, percentual_desconto):
    desconto = preco_original * percentual_desconto / 100
    return desconto

def calcular_preco_final(preco_original, percentual_desconto):
    desconto = calcular_desconto(preco_original, percentual_desconto)
    preco_final = preco_original - desconto
    return preco_final, desconto

# Entrada de dados
preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (ex: 10): "))

# Cálculo
preco_final, valor_desconto = calcular_preco_final(preco_original, percentual_desconto)

# Resultado
print("\n" + "=" * 50)
print("CÁLCULO DE DESCONTO")
print("=" * 50)
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
print(f"Economia: R$ {valor_desconto:.2f}")
print("=" * 50)