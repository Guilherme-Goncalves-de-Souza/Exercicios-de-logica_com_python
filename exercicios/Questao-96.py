def Media(n1, n2):
    media = (n1 + n2) / 2
    return media

number1 = float(input('Digite o 1° número: '))
number2 = float(input('Digite o 2° número: '))
print(f'A média entre {number1} e {number2} é de {Media(number1, number2): .2f}!')