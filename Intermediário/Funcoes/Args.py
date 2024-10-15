x, y, *resto = 1, 2, 5, 8

print(x, y, resto)

def soma(*args):
    total = 0
    for n in args:
        total+=n
    return total

print(soma(10,10,10,20,20))