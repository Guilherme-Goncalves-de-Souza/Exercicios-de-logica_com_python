def Maior(n1, n2):
    if(n1 > n2):
        print(f'O {n1} é MAIOR que {n2}!')
    elif(n2 > n1):
        print(f'O {n2} é MAIOR que {n1}!')
    elif(n1 == n2):
        print(f'O {n1} é IGUAL ao {n2}!')

number1 = int(input('Digite o 1° número inteiro: '))
number2 = int(input('Digite o 2° número inteiro: '))
Maior(number1, number2)