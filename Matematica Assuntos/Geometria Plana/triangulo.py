selecionar_formula = input("Informe a formula a seguir:\nA ==> área\nP ==> perimetro\n==>: ").upper()

#Formula Área
if selecionar_formula == "A":
    base = float(input("Informe a base do triangulo: "))
    altura = float(input("Informe a altura do triangulo: "))
    area = (base * altura) / 2
    print(f"A área do triangulo é: {round(area, 2)}")
#Formula do perímetro
elif selecionar_formula == "P":
    valor_a = float(input("Informe o valor de a: "))
    valor_b = float(input("Informe o valor de b: "))
    valor_c = float(input("Informe o valor de c: "))
    perimetro = valor_a + valor_b + valor_c
    print(f"O perimetro do triangulo é: {perimetro}")
else:
    print("Erro, formula inválida!")