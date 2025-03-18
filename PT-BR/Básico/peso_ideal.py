altura = float(input("Informe a sua altura: "))
selecionar_genero = input("Informe seu genero (M/F): ").upper()

print(f"O peso do ideal do homem é {round((72.7 * altura) - 58 , 2)}" if selecionar_genero == "M" else f"O peso ideal da mulher é {round((62.1 * altura) - 44.7 , 2)}" if selecionar_genero == "F" else "Genero inválido!")