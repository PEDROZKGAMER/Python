Letras = []

contador = 1
continuar_letra = True
while(continuar_letra):
    letra = input(f"Informe a {contador}° letra: ")

    if(letra == "" or not all(verificar.isalpha() or verificar.isspace() for verificar in letra)):
        print("Letra não digitada ou invalida!")
        continue

    Letras.append(letra)

    while(True):
        sair = input("Deseja inserir outra letra? (S/N): ").upper()

        if(sair == "S"):
            contador += 1
            break
        elif(sair == "N"):
            continuar_letra = False
            break
        else:
            print("Opção inválida!")
            continue

while(True):
    escolha = input("Deseja em ordem crescente ou decrescente? (C/D): ").upper()

    if(escolha == "C"):
        print(f"Ordem crescente!\n{sorted(Letras)}")
        break
    elif(escolha == "D"):
        print(f"Ordem decrescente!\n{sorted(Letras, reverse=True)}")
        break
    else:
        print("Opção inválida!")
        continue