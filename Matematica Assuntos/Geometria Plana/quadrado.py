import math

selecionar_formula = input("Informe a fórmula a seguir:\nA --> área\nP --> perímetro\nD --> diagonal\n-->: ").upper()

if selecionar_formula == "A":
    lado = float(input("Informe o lado do quadrado: "))
    formula_area = lado * lado
    print(f"A área do quadrado é: {formula_area}")
    
elif selecionar_formula == "P":
    lado = float(input("Informe o lado do quadrado: "))
    formula_perimetro = 4 * lado
    print(f"O perímetro do quadrado é: {formula_perimetro}")

elif selecionar_formula == "D":
    lado = float(input("Informe o lado do quadrado: "))
    # Função para fatorar números em primos
    def fatorar_primos(num):
        fatores = {}
        divisor = 2
        while num > 1:
            while num % divisor == 0:
                fatores[divisor] = fatores.get(divisor, 0) + 1
                num //= divisor
            divisor += 1
        return fatores

    # Função para calcular a diagonal
    def calcular_diagonal(lado):
        if lado <= 0:
            return "O valor inserido foi 0 ou inválido!"
        
        # Cálculo da soma dos quadrados
        formula_diagonal1 = (lado * lado) + (lado * lado)

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
    print(f"A diagonal do quadrado é: {resultado}")

else:
    print("Erro: fórmula inválida!")
