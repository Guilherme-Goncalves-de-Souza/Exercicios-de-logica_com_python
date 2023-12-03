listaNumeros = [1, 1]

numerosSequencia = int(input('Digite quantos elementos apareceram: '))

for i in range(1, (numerosSequencia + 1), 1):
    numero = listaNumeros[-1] + listaNumeros[-2]
    listaNumeros.append(numero)

print(listaNumeros)
