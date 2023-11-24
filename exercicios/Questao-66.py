numero = int(input('Digite um número: '))
vezes_multiplicacao = int(input('Digite quantas vezes o número será multiplicado: '))

for i in range(1, (vezes_multiplicacao + 1), 1):
    print(f'{numero} x {i} = {(numero * i)}')