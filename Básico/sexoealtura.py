sexos = []
alturas = []
masculino = 0
feminino = 0

quantidade_pessoas = int(input("Informe a quantidade de pessoas: "))

for x in range(quantidade_pessoas):
    sexo = input("Informe seu sexo: ").upper()
    altura = float(input("Informe a sua altura: "))
    sexos.append(sexo)
    alturas.append(altura)
    
    if sexo == "M":
        masculino += 1
    elif sexo == "F":
        feminino += 1
    else:
        print("Sexo inválido!")
        exit()
        
    if altura >= 2.21:
        print("Altura inválida! Tente novamente.")
        exit()

somar_alturas = sum(alturas)
somar = masculino + feminino
media = somar_alturas / somar

print("-"*100)
print(f"Os sexos {sexos}, As alturas {alturas} ")
print(f"Quantidade masculino {masculino}")
print(f"Quantidade feminino {feminino}")
print(f"A média de sexos e de alturas: {round(media, 2)}")
print("-"*100)