'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''

senha = input("Digite a senha: ")

if len(senha) < 8:
    print("Senha inválida: deve ter pelo menos 8 caracteres.")
else:
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if not tem_numero:
        print("Senha inválida: deve conter pelo menos um número.")
    else:
        print("Senha válida.")