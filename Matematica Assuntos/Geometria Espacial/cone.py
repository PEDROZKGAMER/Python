selecionar_formula = input("Informe a formula a seguir:\nAB ==> área da base\nAL ==> area lateral\nAT ==> area total\nV ==> volume\n==>: ").upper()

#Formula da área lateral
if selecionar_formula == "AL":
    raio = float(input("Informe o raio do cone: "))
    geratriz = float(input("Informe a geratriz do cone: "))
    area_lateral = (3.14 * (raio * geratriz))
    print(f"A área lateral do cone é: {round(area_lateral, 2)}")
#Formula da área total
elif selecionar_formula == "AT":
    raio = float(input("Informe o raio do cone: "))
    geratriz = float(input("Informe a geratriz do cone: "))
    area_total = (3.14 * (raio * raio)) + (3.14 * (raio * geratriz))
    print(f"A área total do cone é: {round(area_total, 2)}")
#Formula do volume
elif selecionar_formula == "V":
    raio = float(input("Informe o raio do cone: "))
    altura = float(input("Informe a altura do cone: "))
    volume = (1/3 * (3.14 * ((raio * raio) * altura)))
    print(f"O volume do cone é: {round(volume, 2)}")
#Formula da área da base
elif selecionar_formula == "AB":
    raio = float(input("Informe o raio do cone: "))
    area_base = 3.14 * (raio * raio)
    print(f"A area base do cone é: {round(area_base, 2)}")
else:
    print("Erro, formula inválida!")