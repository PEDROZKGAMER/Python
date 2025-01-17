selecionar_formula = input("Informe a formula a seguir:\nAL --> área lateral\nAB --> área base\nV --> volume\n-->: ").upper()

if selecionar_formula == "AL":
    base = float(input("Informe a base da piramide: "))
    altura = float(input("Informe a altura da piramide: "))
    area_lateral = (base * altura) / 2
    print(f"A area lateral da piramide é: {area_lateral}")
elif selecionar_formula == "V":
    area_base = float(input("Informe a area base da piramide: "))
    altura = float(input("Informe a altura da piramide: "))
    volume = (area_base * altura) / 3
    print(f"O volume da piramide é: {volume}")
elif selecionar_formula == "AB":
    selecionar_base = input("Informe a base a seguir\nBQ --> base quadrada\nBR --> base retangular\nBT --> base triangular\n-->: ").upper()
    if selecionar_base == "BQ":
        lado = float(input("Informe o lado da base do quadrangular da piramide: "))
        base_quadrada = lado * lado
        print(f"A base quadrangular da piramide é: {base_quadrada}")
    elif selecionar_base == "BR":
        largura = float(input("Informe a largura da base retangular da piramide: "))
        comprimento = float(input("Informe o comprimento da base retangular da piramide: "))
        base_retangular = largura * comprimento
        print(f"A base retangular da piramide é: {base_retangular}")
    elif selecionar_base == "BT":
        base = float(input("Informe a base da piramide: "))
        altura = float(input("Informe a altura da piramide: "))
        base_triangular = (base * altura) / 2
        print(f"A base triangular da piramide é: {base_triangular}")
    else:
        print("Erro, formula inválida!")
else:
    print("Erro, formula inválida!")