listaValoresSequencia = []

primeiroTermo = int(input('Digite o PRIMEIRO TERMO da PA: '))
razao = int(input('Digite a RAZÃO da PA: '))
listaValoresSequencia.append(primeiroTermo)

for i in range(2, 11, 1):
    numero = primeiroTermo + ((i-1) * razao)
    listaValoresSequencia.append(numero)

print(f'PA: {listaValoresSequencia}.')
print(f'A soma dos termos é de: {sum(listaValoresSequencia)}!')