letra = input("Informe uma letra: ")

vogais = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u')

if letra in vogais:
    print("A letra digitada é uma vogal!")
else:
    print("A letra digitada é uma consoante!")