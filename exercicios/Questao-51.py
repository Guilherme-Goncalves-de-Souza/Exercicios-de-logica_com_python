listaNumeros = []

for i in range(1, 9, 1):
    numeros = float(input(f'Digite o preço do produto {i}: '))
    listaNumeros.append(numeros)

print(listaNumeros)
print('O MAIOR preço foi o: R$%.2f' % max(listaNumeros))
print('O MENOR preço foi o: R$%.2f' % min(listaNumeros))
