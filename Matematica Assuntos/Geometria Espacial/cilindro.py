selecionar_formula = input("Informe a formula a seguir:\nAb --> Área da base\nAl --> Área lateral\nAt --> Área total\nV --> volume)\n-->: ").upper()

if selecionar_formula == "AB":
    raio = float(input("Informe o raio do cilindro: "))
    area_base = 3.14 * (raio * raio)
    print(f"A área da base é: {round(area_base, 2)}")
elif selecionar_formula == "AL":
    raio_l = float(input("Informe o raio do cilindro: "))
    altura_l = float(input("Informe a altura do cilindro: "))
    area_lateral = (2 * (3.14 * (raio_l * altura_l)))
    print(f"A área lateral do cilindro é: {area_lateral}")
elif selecionar_formula == "AT":
    base_maior = float(input("Informe a base maior do cilindro: "))
    area_lateral_at = float(input("Informe a area lateral do cilindro: "))
    area_total = ((2 * base_maior) + area_lateral_at)
    print(f"A area total do cilindro é: {area_total}")
elif selecionar_formula == "V":
    base = float(input("Informe a base maior do cilindro: "))
    altura_v = float(input("Informe a altura do cilindro: "))
    volume = (3.14 * (altura_v * (base * base)))
    print(f"O volume do cilindro é: {volume}")
else:
    print("Erro, formula inválida!")