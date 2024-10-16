s1 = set()

#add
s1.add('Julio')
s1.add(1)

#update
#s1.update('Olá, mundo') # passa letra por letra
s1.update(('Olá, mundo', 1, 2, 3, 4))

# s1.clear() # limpa o set

#discard
s1.discard('Olá, mundo') # tira o que for passado no parênteses

print(s1)