pessoa = {
    'nome': 'julio',
    'sobrenome': 'figueiredo',
}

#print(len(pessoa)) # retorna a quantidade de chaves
#print(pessoa.keys()) # mostra as chaves
#print(pessoa.values()) # mostra os valores das chaves
print(pessoa.items())

pessoa.setdefault('idade', '500') # adiciona um valor se a chave não existir
print(pessoa)