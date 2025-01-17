selecionar_formula = input("Informe a formula a seguir:\nA --> área\nP --> perímetro\nBM --> Base média do trapézio\n-->: ").upper()

if selecionar_formula == "A":
    base_maior = float(input("Informe a base maior do trapézio: "))
    base_menor = float(input("Informe a base menor do trapézio: "))
    altura = float(input("Informe a altura do trapézio: "))
    area = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {area}")
elif selecionar_formula == "P":
    base_maior_p = float(input("Informe a base maior do trapézio: "))
    base_menor_p = float(input("Informe a base menor do trapézio: "))
    lado_1 = float(input("Informe a altura do trapézio: "))
    lado_2 = float(input("Informe a altura do trapézio: "))
    perimetro = base_maior_p + base_menor_p + lado_1 + lado_2
    print(f"O perimetro do trapézio é: {perimetro}")
elif selecionar_formula == "BM":
    base_maior_d = float(input("Informe a base maior do trapézio: "))
    base_menor_d = float(input("Informe a base menor do trapézio: "))
    base_media = (base_maior_d * base_menor_d) / 2
    print(f"A base média do trapézio é: {base_media}")
else:
    print("Erro, formula inválida...")

