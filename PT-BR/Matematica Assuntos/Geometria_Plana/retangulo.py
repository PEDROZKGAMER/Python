import math
selecionar_formula = input("Informe a formula a seguir:\nA ==> área\nP ==> perímetro\nD ==> diagonal\n==>: ").upper()

#Formula Área
if selecionar_formula == "A":
    base = float(input("Informe a base do retangulo: "))
    altura = float(input("Informe a altura do retangulo: "))
    area = base * altura
    print(f"A área do retangulo é: {area}")
#Formula do perímetro
elif selecionar_formula == "P":
    base = float(input("Informe a base do retangulo: "))
    altura = float(input("Informe a altura do retangulo: "))
    perimetro = 2 * (base + altura)
    print(f"O perímetro do retangulo é: {perimetro}")
#Formula da diagonal
elif selecionar_formula == "D":
    base = float(input("Informe a base do retangulo: "))
    altura = float(input("Informe a altura do retangulo: "))
    diagonal = math.sqrt((base * base) + (altura * altura))
    print(f"A diagonal do retangulo é: {round(diagonal, 2)}")
else:
    print("Erro, formula inválida!")