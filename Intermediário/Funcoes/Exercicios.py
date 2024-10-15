# criar uma função que retorna números multiplicados


def mult(*args):
    total = 1
    for n in args:
        total *= n
    return total

result = (mult(1, 2, 3, 4, 5))
print(result)

def impar_par(num):
    if num % 2 == 0:
        return 'par'
    
    return 'ímpar'

print(impar_par(4))

def conta_vogais(str):
    vogais = ['a', 'e', 'i', 'o', 'u']
    total_vogais = 0
    for letra in str:
        for vogal in vogais:
            if letra == vogal:
                total_vogais += 1
                
    return f'A palavra {str} tem {total_vogais} vogais'

print(conta_vogais('abelha'))            