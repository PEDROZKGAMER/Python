import math
selecionar_formula = input("Informe a formula a seguir, onde A --> área, P --> perímetro, D --> diagonal: ").upper()

if selecionar_formula == "A":
    base = float(input("Informe a base do retangulo: "))
    altura = float(input("Informe a altura do retangulo: "))
    area = base * altura
    print(f"A área do retangulo é: {area}")

elif selecionar_formula == "P":
    base_p = float(input("Informe a base do retangulo: "))
    altura = float(input("Informe a altura do retangulo: "))
    perimetro = 2 * (base_p + altura)
    print(f"O perímetro do retangulo é: {perimetro}")

elif selecionar_formula == "D":
    base_d = float(input("Informe a base do retangulo: "))
    altura_d = float(input("Informe a altura do retangulo: "))
    resultado = (base_d * base_d) + (altura_d * altura_d)
    diagonal = math.sqrt(resultado)
    print(f"A diagonal do retangulo é: {round(diagonal, 2)}")
else:
    print("Erro, formula inválida!")