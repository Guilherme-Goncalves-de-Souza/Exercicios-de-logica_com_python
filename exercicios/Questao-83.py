listaNumeros = []

from random import randint

def posicaoVetores():
    for i in range(21):
        print(f'{i:4}', end='')

for i in range(21): #É 20
    numeroAleatorio = randint(0, 99)
    listaNumeros.append(numeroAleatorio)

print(listaNumeros)
posicaoVetores()
print()
print()
print('------------------- VALORES ORDENADOS -------------------')
print(sorted(listaNumeros, key=int))
posicaoVetores()

