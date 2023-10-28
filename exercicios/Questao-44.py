valorInicial = int(input('Digite o valor INICIAL da contagem:'))
valorFinal = int(input('Digite o valor FINAL da contagem:'))
incremento = int(input('Digite o valor de INCREMENTO da contagem:'))

for i in range(valorInicial, valorFinal, incremento):
    print(i, end=' ')
print('\nAcabou!')
