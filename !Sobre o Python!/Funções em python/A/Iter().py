#Iter: retorna um iterador assícrono para um iteravel assícrono.
#Por exemplo: Obtendo um iterador de uma lista
lista1 = [1, 2, 3]

interador = iter(lista1)

print(next(interador)) #Exibe 1
print(next(interador)) #Exibe 2
print(next(interador)) #Exibe 3
print("\n")
#OBS: se chamarmos de novo o next, ele irá dar erro, pois não haverá outro número.
#Outro exemplo: Iterando sobre uma String

Nome = "Python"

interador_string = iter(Nome)

print(next(interador_string)) #Exibe P
print(next(interador_string)) #Exibe y
print(next(interador_string)) #Exibe t
print(next(interador_string)) #Exibe h
print(next(interador_string)) #Exibe o
print(next(interador_string)) #Exibe n