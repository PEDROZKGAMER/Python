sexos = []
alturas = []

masculino = 0
feminino = 0
soma_altura = 0

quan_de_pessoas = int(input("Informe a quantidade de pessoas: "))

for x in range(quan_de_pessoas):
    sexo = input("Informe o sexo da pessoa (M/F): ")
    altura = float(input("Informe a altura da pessoa: "))
    sexos.append(sexo)
    alturas.append(altura)

    if sexo == "M":
        masculino += 1
    elif sexo == "m":
        masculino += 1
    elif sexo == "F":
        feminino += 1
    elif sexo == "f":
        feminino += 1
    else:
        print("Erro, sexo inválido!")
        exit

    if altura >= 2.20:
        print("Erro, altura inválida!")
    else:
        soma_altura += altura
    
    media = soma_altura / quan_de_pessoas
    
print("\n\n","-"*80)
print("Dados: ")
print(f"A soma das alturas é: {round(soma_altura, 2)}")
print(f"A quanntidade de homens é: {masculino}")
print(f"A quantidade de mulheres é: {feminino}")
print(f"A media é: {round(media, 2)}")
print("-"*80)