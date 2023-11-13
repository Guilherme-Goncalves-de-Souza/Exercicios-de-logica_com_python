soma = 0

print('!SOMADOR DE NÚMEROS!')
print('---------------------')
print('Digite 1111 para parar.')
print('---------------------')


while True:
    numero = int(input('Digite o número a ser somado -> '))

    if(numero == 1111):
        print(f'A soma de todos os números foi de: {soma}')
        print('FIM do programa!')
        break

    soma += numero