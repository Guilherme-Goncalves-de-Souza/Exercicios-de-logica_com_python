listaNumeros = [1, 1]

def Fibonacci(qtdTermos):
    for i in range(qtdTermos - 2):
        number = listaNumeros[-1] + listaNumeros[-2]
        listaNumeros.append(number)

    print(listaNumeros)

quantidadeTermos = int(input('Digite a quantidade de termos que deverá aparecer: '))

if(quantidadeTermos != 1 and quantidadeTermos != 0):
    Fibonacci(quantidadeTermos)
elif(quantidadeTermos == 1):
    print('1')


