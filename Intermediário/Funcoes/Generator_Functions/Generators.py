# São funções que "pausam" 

def generator(n=0):
    yield 1 # pausar
    print("Continua")
    yield 2 # pausar
    print("mais uma")
    yield 3
    print('fim')
    return 'acabou'

gen = generator(n=0)
print(next(gen)) # chamou o 1
print(next(gen)) # chama o continua e o 2
print(next(gen)) # chama mais uma e 3
print(next(gen)) # chama o fim

for n in gen:
    print(n)