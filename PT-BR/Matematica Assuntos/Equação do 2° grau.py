import math

valor_a = int(input("Informe um valor: "))
valor_b = int(input("Informe um valor: "))
valor_c = int(input("Informe um valor: "))

print("\nPasso a passo completo: ")
print("\nIndentificar o valor delta!")
print(f"Δ = {valor_b}² - 4 * {valor_a} * ({valor_c})")

delta = (valor_b * valor_b) - (4 * valor_a * valor_c)

print(f"Δ = {valor_b * valor_b} - ({4 * valor_a * valor_c})")
print(f"Δ = {delta}")

print("\nResolvendo o X!")
print(f"X = -({valor_b}) ± √{delta} / 2 * {valor_a}")

x1 = (-valor_b + math.sqrt(delta)) / (2 * valor_a)
x2 = (-valor_b - math.sqrt(delta)) / (2 * valor_a)

print(f"X = {-(valor_b)} ± {int(math.sqrt(delta))} / {2 * valor_a}")

print("\nValor do X¹!")
print(f"X¹ = {(-(valor_b))} + {int(math.sqrt(delta))} / {(2 * valor_a)}")
print(f"X¹ = {x1}")

print("\nValor do X²!")
print(f"X² = {(-(valor_b))} - {int(math.sqrt(delta))} / {(2 * valor_a)}")
print(f"X² = {x2}")