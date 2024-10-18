import random

# Criar a lista de jogadores
jogadores = []
for i in range(4):
    jogador = {}  # Reinicializa o dicionário a cada iteração
    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['numero_sort'] = random.randint(1, 6)
    jogadores.append(jogador)

# Ordenar a lista com base no número sorteado
jogadores.sort(key=lambda x: x['numero_sort'], reverse=True)

# Exibir o resultado com as colocações
colocacao = 1
for jogador in jogadores:
    print(f'{colocacao}º lugar: {jogador["nome"]} - número sorteado: {jogador["numero_sort"]}')
    colocacao += 1
