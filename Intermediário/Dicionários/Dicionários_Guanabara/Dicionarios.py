dados = {
    'nome': 'julio',
    'idade': 18
}

#print(dados['nome'])

dados['sexo'] = 'M' # adicionar elementos

#print(dados)

filmes = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

#print(filmes.values()) # printa só os valores, ali do lado direito no caso
#print(filmes.keys()) # printa só as chaves, ali do lado esquerdo no caso
#print(filmes.items())

for k,v in filmes.items(): # k = key, v = value
    print(f'O {k} é {v}')
    
brasil = []
estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'uf': 'São paulo',
    'sigla': 'SP'
}
brasil.append(estado1)
brasil.append(estado2)
#print(brasil)
#print(brasil[0])
#print(brasil[0]['uf'])

estados = dict()
brasa = list()
for i in range (3):
    estados['uf'] = str(input('Digite a Unidade Federativa: '))
    estados['sigla'] = str(input('Digite a sigla: '))
    brasa.append(estados.copy())
for e in brasa:
    print(e)