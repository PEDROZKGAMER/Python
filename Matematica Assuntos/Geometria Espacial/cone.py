selecionar_formula = input("Informe a formula a seguir:\nAB --> área da base\nAL --> area lateral\nAT --> area total\nV --> volume\n-->: ").upper()

if selecionar_formula == "AL":
    raio = float(input("Informe o raio do cone: "))
    geratriz = float(input("Informe a geratriz do cone: "))
    area_lateral = (3.14 * (raio * geratriz))
    print(f"A área lateral do cone é: {area_lateral}")
elif selecionar_formula == "AT":
    raio = float(input("Informe o raio do cone: "))
    geratriz = float(input("Informe a geratriz do cone: "))
    area_total = (3.14 * (raio * raio)) + (3.14 * (raio * geratriz))
    print(f"A área total do cone é: {area_total}")
elif selecionar_formula == "V":
    raio = float(input("Informe o raio do cone: "))
    altura = float(input("Informe a altura do cone: "))
    volume = (1/3 * (3.14 * ((raio * raio) * altura)))
    print(f"O volume do cone é: {volume}")
elif selecionar_formula == "AB":
    raio = float(input("Informe o raio do cone: "))
    area_base = 3.14 * (raio * raio)
    print(f"A area base do cone é: {area_base}")
else:
    print("Erro, formula inválida!")