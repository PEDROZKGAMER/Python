raio = float(input("Informe o raio do circulo: "))
selecionar_formula = input("Informe qual formula você queira onde  A ou a -> área || P ou p -> perímetro || D ou d -> diametro ||: ").upper()
pi = 3.14

area = "A"
perimetro = "P"
diametro = "D"

formula_area = pi * (raio * raio)
formula_perimetro = 2 * pi * raio
formula_diametro = 2 * raio

if selecionar_formula == area:
    print(f"{formula_area}cm²")
elif selecionar_formula == perimetro:
    print(f"{formula_perimetro}")
elif selecionar_formula == diametro:
    print(f"{formula_diametro}")
else:
    print("Erro, formula inválida!")