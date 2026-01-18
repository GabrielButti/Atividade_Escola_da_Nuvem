'''4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
'''

from datetime import datetime

def calcular_dias_vivo(data_nascimento):
    data_hoje = datetime.now()
    dias_vivo = (data_hoje - data_nascimento).days
    return dias_vivo

def calcular_anos_meses_dias(data_nascimento):
    data_hoje = datetime.now()
    
    anos = data_hoje.year - data_nascimento.year
    meses = data_hoje.month - data_nascimento.month
    dias = data_hoje.day - data_nascimento.day
    
    if dias < 0:
        meses -= 1
        dias += 30
    
    if meses < 0:
        anos -= 1
        meses += 12
    
    return anos, meses, dias

# Entrada de dados
print("Digite sua data de nascimento:")
dia = int(input("Dia (1-31): "))
mes = int(input("Mês (1-12): "))
ano = int(input("Ano (YYYY): "))

try:
    data_nascimento = datetime(ano, mes, dia)
    
    # Cálculos
    dias_vivo = calcular_dias_vivo(data_nascimento)
    anos, meses, dias = calcular_anos_meses_dias(data_nascimento)
    
    # Resultado
    print("\n" + "=" * 50)
    print("TEMPO DE VIDA")
    print("=" * 50)
    print(f"Data de nascimento: {data_nascimento.strftime('%d/%m/%Y')}")
    print(f"\nVocê está vivo há:")
    print(f"  {anos} anos, {meses} meses e {dias} dias")
    print(f"  Total de dias: {dias_vivo} dias")
    print("=" * 50)
    
except ValueError:
    print("Data inválida! Verifique os valores inseridos.")