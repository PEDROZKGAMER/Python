import math

lado = float(input("informe o lado do quadrado: "))
selecionar_formula = input("Informe a formula onde (A ou a --> área || P ou p --> perímetro): ").upper()

formula_area = lado * lado
formula_perimetro = 4 * lado

#Formula da diagonal:
def fatorar_primos(num):
    fatores = {}
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            fatores[divisor] = fatores.get(divisor, 0) + 1
            num //= divisor
        divisor += 1
    return fatores

def calcular_diagonal(lado):
    if lado <= 0:
        return "O valor inserido foi 0 ou inválido!"
    
    # Cálculo da soma dos quadrados
    formula_diagonal1 = ((lado * lado) + (lado * lado))

    # Fatoração do valor da soma dos quadrados
    fatores = fatorar_primos(formula_diagonal1)
    dentro_da_raiz = []
    fora_da_raiz = 1

    for fator, potencia in fatores.items():
        pares = potencia // 2
        sobrou = potencia % 2

        fora_da_raiz *= fator ** pares
        if sobrou > 0:
            dentro_da_raiz.append(fator)

    # Retorna o resultado formatado
    if dentro_da_raiz:
        return f"D = {fora_da_raiz}√({' * '.join(map(str, dentro_da_raiz))})"
    else:
        return f"D = {fora_da_raiz}"

resultado = calcular_diagonal(lado)

if selecionar_formula == "A":
    print(f"{formula_area}")
elif selecionar_formula == "P":
    print(f"{formula_perimetro}")
elif selecionar_formula == "D":
    print(f"{resultado}")
else:
    print("Erro, formula inválida!")

