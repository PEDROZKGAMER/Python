nome = input("Informe seu nome: ").upper()

soma_nota = 0
contador = 1

while(contador <= 4):
    nota = float(input("Informe o valor: "))

    if(nota < 0 or nota > 10):
        print("Erro, nota inválida!! Por favor informar um nota válida!")
        continue
    
    soma_nota += nota
    contador += 1
media = (soma_nota / 4)

print(f"{nome} você foi reprovado, pois {media:.2f}" if media <= 4 else f"{nome} você esta na final pois {media:.2f}" if media > 4.0 and media < 7.0 else f"{nome} você foi aprovado pois {media:.2f}")