letras = set()

while True:
    
    letra = input('Digite: ')
    letras.add(letra)
    print(letras)
    
    if 'z' in letras:
        break
    
# nesse caso ele nao conta as letras repetidas