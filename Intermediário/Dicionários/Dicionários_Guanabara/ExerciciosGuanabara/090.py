aluno = dict()

aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = int(input('Digite a média: '))

def situacao(media):
    if media>=5:
        return 'Aprovado!'
    return 'Reprovado!'

print(situacao(aluno['media']))