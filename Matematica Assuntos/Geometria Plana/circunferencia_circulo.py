selecionar_formula = input("Informe a formula a seguir:\nA ==> área\nP ==> perímetro\nD ==> diametro\n==>: ").upper()

#Formula Área
if selecionar_formula == "A":
    raio = float(input("Informe o raio do circulo: "))
    formula_area = 3.14 * (raio * raio)
    print(f"{round(formula_area, 2)}cm²")
#Formula do perímetro
elif selecionar_formula == "P":
    raio = float(input("Informe o raio do circulo: "))
    formula_perimetro = 2 * 3.14 * raio
    print(f"{round(formula_perimetro, 2)}")
#Formula da diagonal
elif selecionar_formula == "D":
    raio = float(input("Informe o raio do circulo: "))
    formula_diametro = 2 * raio
    print(f"{formula_diametro}")
else:
    print("Erro, formula inválida!")
