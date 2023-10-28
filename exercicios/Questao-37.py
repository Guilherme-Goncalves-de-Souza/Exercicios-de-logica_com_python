print('!PROGRAMA NOVO SALÁRIO!')

salarioAtual = float(input('Digite o salário atual: '))
generoFunc = input('Digite o gênero (M/masculino ou F/feminino):')
anosServico = float(input('Digite a quantidade de anos trabalhos na empresa:'))

generoMas = {'M', 'Masculino', 'm', 'masculino'}
generoFem = {'F', 'Feminino', 'f', 'feminino'}


if(generoFunc in generoFem):
    if (anosServico <= 15):
        aumento = salarioAtual * 0.05
        salarioAtualizado = salarioAtual + aumento
        print(f'O aumento será de {aumento}')
        print('O salário ajustado ficou em %.2f' % salarioAtualizado)
    elif(anosServico > 15 and anosServico <= 20):
        aumento = salarioAtual * 0.12
        salarioAtualizado = salarioAtual + aumento
        print(f'O aumento será de {aumento}')
        print('O salário ajustado ficou em %.2f' % salarioAtualizado)
    else:
        aumento = salarioAtual * 0.23
        salarioAtualizado = salarioAtual + aumento
        print(f'O aumento será de {aumento}')
        print('O salário ajustado ficou em %.2f' % salarioAtualizado)

elif(generoFunc in generoMas):
    if (anosServico <= 20):
        aumento = salarioAtual * 0.03
        salarioAtualizado = salarioAtual + aumento
        print(f'O aumento será de {aumento}')
        print('O salário ajustado ficou em %.2f' % salarioAtualizado)
    elif (anosServico > 20 and anosServico <= 30):
        aumento = salarioAtual * 0.13
        salarioAtualizado = salarioAtual + aumento
        print(f'O aumento será de {aumento}')
        print('O salário ajustado ficou em %.2f' % salarioAtualizado)
    else:
        aumento = salarioAtual * 0.25
        salarioAtualizado = salarioAtual + aumento
        print(f'O aumento será de {aumento}')
        print('O salário ajustado ficou em %.2f' % salarioAtualizado)