def Somador(n1, n2):
    soma = n1 + n2
    return soma

number1 = int(input('Digite o 1° número: '))
number2 = int(input('Digite o 2° número: '))
print(f'A soma entre {number1} + {number2} é de: {Somador(number1, number2)}!')