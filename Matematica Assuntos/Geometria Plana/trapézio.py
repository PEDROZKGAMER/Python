selecionar_formula = input("Informe a formula a seguir:\nA ==> área\nP ==> perímetro\nBM ==> Base média do trapézio\n==>: ").upper()

#Formula Área
if selecionar_formula == "A":
    base_maior = float(input("Informe a base maior do trapézio: "))
    base_menor = float(input("Informe a base menor do trapézio: "))
    altura = float(input("Informe a altura do trapézio: "))
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {round(area, 2)}")
#Formula do perímetro
elif selecionar_formula == "P":
    base_maior = float(input("Informe a base maior do trapézio: "))
    base_menor = float(input("Informe a base menor do trapézio: "))
    lado_1 = float(input("Informe a altura do trapézio: "))
    lado_2 = float(input("Informe a altura do trapézio: "))
    perimetro = base_maior + base_menor + lado_1 + lado_2
    print(f"O perimetro do trapézio é: {perimetro}")
#Formula da base média
elif selecionar_formula == "BM":
    base_maior = float(input("Informe a base maior do trapézio: "))
    base_menor = float(input("Informe a base menor do trapézio: "))
    base_media = (base_maior * base_menor) / 2
    print(f"A base média do trapézio é: {round(base_media, 2)}")
else:
    print("Erro, formula inválida...")

