selecionar_formula = input("Informe a formula a seguir:\nAL ==> área lateral\nAB ==> área base\nV ==> volume\n==>: ").upper()

#Formula da área lateral
if selecionar_formula == "AL":
    base = float(input("Informe a base da piramide: "))
    altura = float(input("Informe a altura da piramide: "))
    area_lateral = (base * altura) / 2
    print(f"A area lateral da piramide é: {round(area_lateral, 2)}")
#Formula do volume
elif selecionar_formula == "V":
    area_base = float(input("Informe a area base da piramide: "))
    altura = float(input("Informe a altura da piramide: "))
    volume = (area_base * altura) / 3
    print(f"O volume da piramide é: {round(volume, 2)}")
#Área da base
elif selecionar_formula == "AB":
    selecionar_base = input("Informe a base a seguir\nBQ ==> base quadrada\nBR ==> base retangular\nBT ==> base triangular\n==>: ").upper()
    #Formula da base quadrangular
    if selecionar_base == "BQ":
        lado = float(input("Informe o lado da base do quadrangular da piramide: "))
        base_quadrada = lado * lado
        print(f"A base quadrangular da piramide é: {round(base_quadrada, 2)}")
    #Formula da base retangular
    elif selecionar_base == "BR":
        largura = float(input("Informe a largura da base retangular da piramide: "))
        comprimento = float(input("Informe o comprimento da base retangular da piramide: "))
        base_retangular = largura * comprimento
        print(f"A base retangular da piramide é: {round(base_retangular, 2)}")
    #Formula da base tiangular
    elif selecionar_base == "BT":
        base = float(input("Informe a base da piramide: "))
        altura = float(input("Informe a altura da piramide: "))
        base_triangular = (base * altura) / 2
        print(f"A base triangular da piramide é: {round(base_triangular, 2)}")
    else:
        print("Erro, formula inválida!")
else:
    print("Erro, formula inválida!")