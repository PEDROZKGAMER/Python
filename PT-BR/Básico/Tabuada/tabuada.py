valor = int(input("Informe o numero da tabuada: "))
operador = input("Informe o operador artimético queira calcular, onde(+ ==> soma, - ==> sub, * ==> multi, / ==> div): ")

print("Erro, tabuada inválida!" if valor < 0 else "erro, operador inválido!" if operador not in ["+", "-", "*", "/"] else "\n".join(f"{valor} {operador} {num} = {eval(f'{valor}{operador}{num}')}" for num in range(1, 11)))