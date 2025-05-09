lista = [4, 2, 8, 1, 9]

# Adicionar elementos
lista.append(5)
lista.extend([7, 3])

# Inserir elemento
lista.insert(2, 6)

# Remover elemento
lista.remove(8)

# Ordenar
lista.sort()  # Ordena in-place
nova_lista = sorted(lista, reverse=True)  # Ordena e retorna uma nova lista

print(f"lista normal: {lista}")  # Saída: [1, 2, 3, 4, 5, 6, 7, 9]
print(f"Ordem decrescente: {nova_lista}") # Saída: [9, 7, 6, 5, 4, 3, 2, 1]
print(f"Quantidade: {len(lista)}") # Saída: 8

elemento_removido = lista.pop(2)
print(elemento_removido) #Saida 3

lista_2 = [10, 20, 30, 40, 50]

indice = lista_2.index(20)
print(indice) #Saida 1


lista.clear() #Limpa a lista
print(lista) #saida []