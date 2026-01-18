'''2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.'''

def palindromo(texto):
    """Verifica se um texto é palíndromo, ignorando espaços e pontuação."""
    # Remove espaços e pontuação, e converte para minúsculas
    texto_limpo = ""
    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere.lower()
    
    # Compara o texto com seu reverso
    return texto_limpo == texto_limpo[::-1]

# Entrada de dados
texto = input("Digite uma palavra ou frase: ")

# Verificação
resultado = palindromo(texto)

# Resultado
print("\n" + "=" * 50)
if resultado:
    print("Resposta: Sim")
else:
    print("Resposta: Não")
print("=" * 50)