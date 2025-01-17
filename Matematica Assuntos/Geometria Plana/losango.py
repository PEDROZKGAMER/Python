import math
selecionar_formula = input("Informe a formula a seguir:\nA --> Area\nP --> perimetro\nD --> diagonal\n-->: ").upper()

if selecionar_formula == "A":
    diagonal_maior = float(input("Informe o valor da diagonal maior: "))
    diagonal_menor = float(input("Informe o valor da diagonal menor: "))
    area = (diagonal_maior * diagonal_menor) / 2
    print(f"A área do losango é: {area}")
elif selecionar_formula == "P":
    lado = float(input("Informe o lado do losango: "))
    perimetro = 4 * lado
    print(f"O perímetro do losango é: {perimetro}")
elif selecionar_formula == "D":
    diagonal_maior_D = float(input("Informe o valor da diagonal maior: "))
    diagonal_menor_d = float(input("Informe o valor da diagonal menor: "))
    resultado = math.sqrt((math.pow(diagonal_maior_D / 2, 2)) + (math.pow(diagonal_menor_d / 2, 2)))
    print(f"\nA diagonal do losango: {round(resultado, 2)}")
    print("Atenção: Se você quer saber qual o perímetro a partir da relação entre as diagonais, basta inserir os valores nos campos abaixos e depois que o resultado for exibido ai pegue o valor e coloque no campo onde diz perímetro OK")
else:
    print("Erro, formula inválida")

