Pessoas = []
masculino = 0
feminino = 0
soma_alturas = 0

while(True):
    nome = input("Informe o nome da pessoa: ").upper().strip()

    if(nome == ""):
        print("Nome inválido! Por favor informar o nome correto!")
        continue

    sexo = input(f"Informe o sexo de {nome}: (M/F) ").upper().strip()

    if(sexo == ""):
        print("Sexo inválido! Por favor informar o sexo correto!")
        continue

    if(sexo == "M"):
        masculino += 1
    elif(sexo == "F"):
        feminino += 1
    else:
        print("Erro, sexo inválido! Por favor informar o sexo correto!")
        continue

    altura = float(input(f"Informe a altura de {nome}: "))

    if(altura == "" and altura < 0.5 or altura >= 2.0):
        print("Altura inválida, por favor informar altura correta!")
        continue

    soma_alturas += altura
    media = soma_alturas / (masculino + feminino)

    pessoa = {"Nome": nome,"Sexo": sexo, "Altura": altura}
    Pessoas.append(pessoa)

    sair = input("Deseja informar outra pessoa? (S/N) ").upper()

    if(sair == "N"):
        break

print("\n#==== Lista de pessoas ====#")
for people in Pessoas:
    print(f"Nome: {people['Nome']} || Sexo: {people['Sexo']} || Altura: {people['Altura']}")
print(f"\nQuantidade masculino: {masculino} || Quantidade Feminino: {feminino}\nMédia de pessoas: {round(media, 2)}")