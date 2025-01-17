import math
selecionar_formula = input("Informe a formula a seguir:\nA --> área\nP --> perímetro\nD --> diagonal\n-->: ").upper()

if selecionar_formula == "A":
    base = float(input("Informe a base do paralelograma: "))
    altura = float(input("Informe a altura do paralelograma: "))
    area = base * altura
    print(f"A área do paralelograma é: {area}")
elif selecionar_formula == "P":
    base_p = float(input("Informe a base do paralelograma: "))
    lado = float(input("Informe o lado do paralelograma: "))
    perimetro = 2 * (base_p + lado)
    print(f"O perímetro do paralelograma é: {perimetro}")
else:
    print("Erro, formula inválida")