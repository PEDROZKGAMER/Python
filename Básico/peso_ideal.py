altura = float(input("Informe a sua altura: "))
selecionar_genero = input("Informe seu genero (M/F): ").upper()

if selecionar_genero == "M":
    calculo_homem =  (72.7 * altura) - 58
    print(f"O peso ideal do homem: {round(calculo_homem, 2)}")
elif selecionar_genero == "F":
    calculo_mulher = (62.1 * altura) - 44.7
    print(f"O peso ideal da mulher é: {round(calculo_mulher, 2)}")
else:
    print("Erro, genero inválido!")
