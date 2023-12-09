listaNumeros = []
listaNumerosPares = []

for i in range(10):
    numero = int(input(f'Digite o {i+1}° número: '))
    listaNumeros.append(numero)

    if(numero % 2 == 0):
        listaNumerosPares.append([f'Número PAR: {numero}', f'Na posição {i+1}'])

print(listaNumeros)
for i in range(10):
    print(f'{i:3}', end='')

print()
print()
print(listaNumerosPares)