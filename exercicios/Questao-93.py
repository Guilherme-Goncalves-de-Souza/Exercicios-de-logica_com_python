def Contador(ninicio, nfim, nincremento):
    for i in range(ninicio, nfim, nincremento):
        print(f'{i} >> ', end='')
    print('FIM')

inicio = int(input('Digite o valor de ÍNICIO: '))
fim = int(input('Digite o valor de FIM: '))
incremento = int(input('Digite o valor de INCREMENTO: '))

Contador(inicio, fim, incremento)