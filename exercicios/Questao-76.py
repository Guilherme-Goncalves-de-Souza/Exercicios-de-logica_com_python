from random import randint

for i in range(8):
    listaNumeros = randint(0, 99)
    print(listaNumeros, end=' ')

print()

for i in range(8):
    print(f'{i:3}', end='')