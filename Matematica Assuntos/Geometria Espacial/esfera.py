selecionar_formula = input("Informe a formula a seguir, onde(A --> área, V --> volume): ").upper()

if selecionar_formula == "A":
    raio = float(input("Informe o raio da esfera: "))
    area = 4 * (3.14 * (raio * raio))
    print(f"A área da esfera é: {area}")
elif selecionar_formula == "V":
    raio = float(input("Informe o raio da esfera: "))
    volume = (4 / 3) * 3.14 * (raio ** 3)
    print(f"O volume da esfera é: {round(volume, 2)}")
else:
    print("Erro, formula inválida!")
