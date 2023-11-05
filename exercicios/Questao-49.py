listaPares = []
listaImpares = []

for i in range(1, 7, 1):
    numeros = int(input(f'Digite o número {i}: '))
    if(numeros % 2 == 0):
        listaPares.append(numeros)
    else:
        listaImpares.append(numeros)
print(f'O número de Pares são: {len(listaPares)}, foram eles: {listaPares}')
print(f'O número de Impares são: {len(listaImpares)}, foram eles: {listaImpares}')
