listaNumeros = [1, 1]

for i in range(14):
    number = listaNumeros[-1] + listaNumeros[-2]
    listaNumeros.append(number)
print(listaNumeros)

for i in range(16):
    print(f'{i:4}', end='')