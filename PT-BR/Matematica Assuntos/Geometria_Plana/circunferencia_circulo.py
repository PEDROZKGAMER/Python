selecionar_formula = int(input("Informe a formula a seguir:\n1 ==> área\n2 ==> perímetro\n3 ==> diametro\n4 ==> sair_programa: "))
raio = float(input("Informe o raio do circulo: "))

if(selecionar_formula == 4):
    print("Voltando pro menu...")
    exit()
print(f"A área do circulo é: {round(3.14 * (raio * raio) , 2)}cm²" if selecionar_formula == 1 else f"O perímetro do circulo é: {round(2 * 3.14 * raio , 2)}" if selecionar_formula == 2 else f"O diametro do circulo é: {round(2 * raio , 2)}" if selecionar_formula == 3 else"Erro, formula inválida!")