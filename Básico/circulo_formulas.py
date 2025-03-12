valor = float(input("Informe o raio do circulo: "))
selecionar_formula = input("Informe qual formula você queira onde  A ou a -> área || P ou p -> perímetro || D ou d -> diametro ||: ")
pi = 3.14

area = "A" and "a"
perimetro = "P" and "p"
diametro = "D" and "d"

formula_area = pi * (valor * valor)
formula_perimetro = 2 * pi * valor
formula_diametro = 2 * valor

if selecionar_formula == area:
    print(f"{formula_area}cm²")
elif selecionar_formula == perimetro:
    print(f"{formula_perimetro}")
elif selecionar_formula == diametro:
    print(f"{formula_diametro}")