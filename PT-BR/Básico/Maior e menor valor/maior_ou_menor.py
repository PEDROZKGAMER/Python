numeros = []
contador = 1

continur_registrar = True
while(continur_registrar):
    try:
        numero = int(input(f"Informe o {contador}° numero: "))
    except(ValueError):
        print("O valor deve ser numérico!")
        continue

    numeros.append(numero)

    while(True):
        sair = input("Deseja inserir outro numero? (S/N): ").upper()

        if(sair == "S"):
            contador += 1
            break
        elif(sair == "N"):
            continur_registrar = False
            break
        else:
            print("Opção inválida!")
            continue

while(True):
    escolha = input("Qual deseja escolher o maior ou menor valor? (M/m): ")

    if(escolha == "M"):
        print(f"O valor maior: {max(numeros)}\nQuantidade de numeros digitados: {len(numeros)}")
        break
    elif(escolha == "m"):
        print(f"O valor menor: {min(numeros)}\nQuantidade de numeros digitados: {len(numeros)}")
        break
    else:
        print("Opção inválida!")
        continue