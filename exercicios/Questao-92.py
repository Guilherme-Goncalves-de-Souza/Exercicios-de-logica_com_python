def ParOuImpar(numero):
    if(numero % 2 == 0):
        print(f'O {numero} é PAR!')
    else:
        print(f'O {numero} é IMPAR!')

number = int(input('Digite um número INTEIRO: '))
ParOuImpar(number)