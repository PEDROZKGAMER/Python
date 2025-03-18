import math

selecionar_formula = int(input("Informe a formula abaixo:\n1 ==> Área\n2 ==> P\n3 ==> Diagonal"))
lado = float(input("Informe o lado do quadrado: "))

print(f"A área do quadrado é: {lado * lado}" if selecionar_formula == 1 else f"O perimetro do quadrado é {4 * lado}" if selecionar_formula == 2 else "A diagonal do quadrado é!! em manutencao" if selecionar_formula == 3 else "Erro, formula inválida!")