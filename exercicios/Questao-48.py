soma = 0
listaNumerosEscolhidos = []

for i in range(1, 8, 1):
    numero = int(input(f'Digite o número {i}: '))
    listaNumerosEscolhidos.insert(i, numero)

    soma += numero
print(f'A soma dos números {listaNumerosEscolhidos} foi de:')
print(soma)

