numeros = []

contador = 1
continuar_numero = True
while(continuar_numero):
    try:
        numero = int(input(f"Informe a {contador}° numero: "))
    except(ValueError):
        print("O valor deve ser numérico")
        continue

    numeros.append(numero)

    while(True):
        sair = input("Deseja inserir outra numero? (S/N): ").upper()

        if(sair == "S"):
            contador += 1
            break
        elif(sair == "N"):
            continuar_numero = False
            break
        else:
            print("Opção inválida!")
            continue

while(True):
    escolha = input("Deseja em ordem crescente ou decrescente? (C/D): ").upper()

    if(escolha == "C"):
        print(f"Ordem crescente!\n{sorted(numeros)}")
        break
    elif(escolha == "D"):
        print(f"Ordem decrescente!\n{sorted(numeros, reverse=True)}")
        break
    else:
        print("Opção inválida!")
        continue