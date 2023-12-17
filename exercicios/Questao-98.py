def SuperSomador(intervalo1, intervalo2):
    soma = 0
    for i in range(intervalo1, intervalo2+1, 1):
        soma += i

    return soma

n1 = int(input('Digite o 1° valor do intervalo: '))
n2 = int(input('Digite o 2° valor do intervalo: '))

print(f'A soma de todos os valores no intervalo de: {n1} até {n2}'
      f' é de: {SuperSomador(n1, n2)}')