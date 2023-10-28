print('!PROGRAMA VIDA SAUDÁVEL!')
print('CONSULTE SEUS PONTOS ABAIXO E TROQUE POR DINHEIRO!')

horasAtividade = float(input('Digite a quantidade de HORAS de atividade física no MÊS:'))

if(horasAtividade <= 10):
    pontosGanhos = horasAtividade * 2
    dinheiroGanho = pontosGanhos * 0.05
    print('Você ganhou %.0f pontos' % pontosGanhos)
    print(f'Com eles você ganhou R${dinheiroGanho} reais')
elif(horasAtividade > 10 and horasAtividade <= 20):
    pontosGanhos = horasAtividade * 5
    dinheiroGanho = pontosGanhos * 0.05
    print('Você ganhou %.0f pontos' % pontosGanhos)
    print(f'Com eles você ganhou R${dinheiroGanho} reais')
else:
    pontosGanhos = horasAtividade * 10
    dinheiroGanho = pontosGanhos * 0.05
    print('Você ganhou %.0f pontos' % pontosGanhos)
    print(f'Com eles você ganhou R${dinheiroGanho} reais')

