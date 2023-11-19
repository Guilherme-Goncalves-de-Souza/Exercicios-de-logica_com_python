listaNumeros = []

listaVerificaEncerramento = ['s', 'S', 'sim', 'Sim', 'SIM', 'parar', 'Parar', 'PARAR']

def valoresPares():
    listaValoresPares = []

    for number in listaNumeros:
        if(number % 2 == 0):
            listaValoresPares.append(number)

    print(f'Há {len(listaValoresPares):.0f} números pares, sendo eles: {listaValoresPares}.')

while True:
    numero = float(input('Digite o número: '))
    listaNumeros.append(numero)

    encerrar = input('Deseja parar(S ou N)?')

    if encerrar in listaVerificaEncerramento:
        print(f'A SOMA de todos os números foi de: {sum(listaNumeros):.2f}')
        print(f'O MENOR número digitado foi o: {min(listaNumeros):.2f}')
        print('A média dos valores foi de %.0f.' % (sum(listaNumeros) / len(listaNumeros)))
        valoresPares()
        break