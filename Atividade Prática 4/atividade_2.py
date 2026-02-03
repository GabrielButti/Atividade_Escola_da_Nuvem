'''2 - Criar um código que registre as notas de alunos e calcular a média da turma.
'''

alunos = {}
quantidade_alunos = int(input("Quantos alunos deseja registrar? "))

for i in range(quantidade_alunos):
    nome = input(f"\nDigite o nome do aluno {i + 1}: ")
    notas = []
    
    quantidade_notas = int(input(f"Quantas notas {nome} tem? "))
    
    for j in range(quantidade_notas):
        nota = float(input(f"Digite a nota {j + 1} de {nome}: "))
        notas.append(nota)
    
    media_aluno = sum(notas) / len(notas)
    alunos[nome] = {"notas": notas, "media": media_aluno}

print("\n" + "=" * 50)
print("RESUMO DA TURMA")
print("=" * 50)

for nome, dados in alunos.items():
    print(f"\n{nome}:")
    print(f"  Notas: {dados['notas']}")
    print(f"  Média: {dados['media']:.2f}")

media_turma = sum(dados["media"] for dados in alunos.values()) / len(alunos)
print(f"\n{'=' * 50}")
print(f"Média da turma: {media_turma:.2f}")
print(f"{'=' * 50}")