try:
    print('Abrir arquivo')
    #8 / 0
    
except ZeroDivisionError:
    print("dividiu por zero")
except IndexError as error:
    print('IndexError')    
else:
    print('sem erro')    
finally:   # o finally sempre é executado
    print('Fecha arquivo')
    