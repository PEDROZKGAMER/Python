dados = []

quantidade_numero = int(input("Informe a quantidade de valores: "))
operador = input("Informe o operador aritmético onde (+ -> soma, - -> sub, * -> multi, / -> div, ): ")

soma = '+'
sub = '-'
multi = '*'
div = '/'

feita_conta = False

multiplicar = 1
for x in range(quantidade_numero):
    numero = int(input(f"Informe o {x}° valor: "))
    dados.append(numero)

if operador == soma:
    somar = sum(dados)
    feita_conta = True
    print(somar)

elif operador == sub:
    subtrair = dados[0] - sum(dados[1:])
    feita_conta = True
    print(subtrair)

elif operador == multi:
    for numero in dados:
        multiplicar *= numero
        feita_conta = True

    print(multiplicar)

elif operador == div:
    dividir = dados[0]
    for numero in dados[1:]:
        if numero == 0:
            print("Erro: Divisão por zero!")
            break
        dividir /= numero
        feita_conta = True

    else:
        print(dividir)

if not feita_conta:
    print("Erro, conta inválida!")