selecionar_formula = int(input("Informe a formula a seguir:\n1 ==> Área da base\n2 ==> Área lateral\n3 ==> Área total\n4 ==> volume)\n==>: "))

if(selecionar_formula == 1):
    raio = float(input("Informe o raio do cilindro: "))
elif(selecionar_formula == 2):
    raio = float(input("Informe o raio do cilindro: "))
    altura = float(input("Informe a altura do cilindro: "))
elif(selecionar_formula == 3):
    base_maior = float(input("Informe a base maior do cilindro: "))
    area_lateral = float(input("Informe a area lateral do cilindro: "))
elif(selecionar_formula == 4):
    base = float(input("Informe a base maior do cilindro: "))
    altura = float(input("Informe a altura do cilindro: "))

print(f"A área base do cilindro é: {round(3.14 * (raio * raio), 2)}"if selecionar_formula == 1 else f"A área lateral do cilindro é: {round((2 * (3.14 * (raio * altura))), 2)}" if selecionar_formula == 2 else f"A area total do cilindro é: {((2 * base_maior) + area_lateral)}" if selecionar_formula == 3 else f"O volume do cilindro é: {(3.14 * (altura * (base * base)))}"if selecionar_formula == 4 else "Erro, formula inválida!")