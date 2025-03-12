selecionar_formula = input("Informe a formula a seguir:\nAb ==> Área da base\nAl ==> Área lateral\nAt ==> Área total\nV ==> volume)\n==>: ").upper()

#Formula da area da base
if selecionar_formula == "AB":
    raio = float(input("Informe o raio do cilindro: "))
    area_base = 3.14 * (raio * raio)
    print(f"A área da base é: {round(area_base, 2)}")
#Formula da área lateral
elif selecionar_formula == "AL":
    raio = float(input("Informe o raio do cilindro: "))
    altura = float(input("Informe a altura do cilindro: "))
    area_lateral = (2 * (3.14 * (raio * altura)))
    print(f"A área lateral do cilindro é: {round(area_lateral, 2)}")
#Formula da área total
elif selecionar_formula == "AT":
    base_maior = float(input("Informe a base maior do cilindro: "))
    area_lateral = float(input("Informe a area lateral do cilindro: "))
    area_total = ((2 * base_maior) + area_lateral)
    print(f"A area total do cilindro é: {round(area_total, 2)}")
#Formula do volume
elif selecionar_formula == "V":
    base = float(input("Informe a base maior do cilindro: "))
    altura = float(input("Informe a altura do cilindro: "))
    volume = (3.14 * (altura * (base * base)))
    print(f"O volume do cilindro é: {round(volume, 2)}")
else:
    print("Erro, formula inválida!")