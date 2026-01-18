'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''

temperatura = float(input("Digite a temperatura a ser convertida: "))
unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()

if unidade_origem == 'C':
    if unidade_destino == 'F':
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == 'K':
        temperatura_convertida = temperatura + 273.15
    else:
        temperatura_convertida = temperatura

elif unidade_origem == 'F':
    if unidade_destino == 'C':
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == 'K':
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        temperatura_convertida = temperatura

elif unidade_origem == 'K':
    if unidade_destino == 'C':
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == 'F':
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        temperatura_convertida = temperatura

else:
    print("Unidade de origem inválida!")
    exit()

print(f"\n{temperatura}°{unidade_origem} = {temperatura_convertida:.2f}°{unidade_destino}")