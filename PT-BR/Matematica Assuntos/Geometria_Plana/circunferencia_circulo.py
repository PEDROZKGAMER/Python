selecionar_formula = input("Informe a formula a seguir:\nA ==> área\nP ==> perímetro\nD ==> diametro\n==>: ").upper()
raio = float(input("Informe o raio do circulo: "))

print(f"A área do circulo é: {round(3.14 * (raio * raio) , 2)}cm²" if selecionar_formula == "A" else f"O perímetro do circulo é: {round(2 * 3.14 * raio , 2)}" if selecionar_formula == "P" else f"O diametro do circulo é: {round(2 * raio , 2)}" if selecionar_formula == "D" else "Erro, formula inválida!")