lado = float(input("informe o lado do quadrado: "))
selecionar_formula = input("Informe a formula onde (A ou a --> área || P ou p --> perímetro): ")

area = "A" and "a"
perimetro = "P" and "p"

formula_area = lado * lado
formula_perimetro = 4 * lado

if selecionar_formula == area:
    print(f"{formula_area}")
elif selecionar_formula == perimetro:
    print(f"{formula_perimetro}")
else:
    print("Erro, formula não existe!")
    exit()