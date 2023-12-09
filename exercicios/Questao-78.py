listaNumeros = []
posicoesNumerosDivi10 = []

for i in range(15):
    numero = int(input(f'Digite o {i+1}° número: '))
    listaNumeros.append(numero)

    if(numero % 10 == 0):
        posicoesNumerosDivi10.append(i)

print(listaNumeros)

for i in range(15):
    print(f'{i:3}', end=' ')

print()
print(f'A posições dos números múltiplos de 10 são as: {posicoesNumerosDivi10}')
