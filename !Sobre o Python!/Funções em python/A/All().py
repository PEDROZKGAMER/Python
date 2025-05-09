#A função all() verifica se todos os elementos de um iterável (como lista, tupla, etc) são "verdadeiros" — ou seja, não são False, None, 0, string vazia '', etc.
print("Exemplo 1:")
print(all([True, True, True]))      # True
print(all([True, False, True]))     # False
print(all([1, 2, 3]))               # True (todos são números != 0)
print(all([1, 0, 3]))               # False (0 é falso)
print(all([]))                     # True (iterável vazio -> padrão lógico)
print("\n")


