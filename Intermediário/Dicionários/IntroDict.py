# par de chave e valor

pessoa = {
    'nome': 'julio',
    'sobrenome': 'figueiredo',
    'idade': 18,
    'altura': 1.8,
    'endereço': [
        {'rua': 'tal', 'numero': 123},
        {'rua': 'taltal', 'numero': 132}
    ]
}

pessoa2 = dict(nome='julio', sobrenome ='figueiredo')

print(pessoa)
#print(pessoa2)

print(pessoa['nome'])

