lista = [10, 20, 30, 40]

# insert (indice, valor)
# adiciona um item no indice mas nao apaga o número que está no índice atual
# lista.insert(0, 5)

lista_a = [1,2,3]
lista_b = [4,5,6]

lista_c = lista_a + lista_b

# nao pode jogar o valor em uma variável pois nao retorna nada
lista_a.extend(lista_b)

#print(lista)

print(lista_c)
print(lista_a)