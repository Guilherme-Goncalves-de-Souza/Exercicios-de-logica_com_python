valorInicial = int(input('Digite o valor INICIAL da contagem:'))
valorFinal = int(input('Digite o valor FINAL da contagem:'))

while valorInicial > valorFinal:
    try:
        valorFinal = int(input('Digite o valor FINAL menor que %.0f:' % valorInicial))
        if valorInicial < valorFinal:
            break
        else:
            print('Você ainda digitou o número FINAL maior que o inicial!')
    except ValueError:
        print('Digite um número válido!')

incremento = int(input('Digite o valor de INCREMENTO da contagem:'))



for i in range(valorInicial, valorFinal, incremento):
    print(i, end=' ')
print('\nAcabou!')
