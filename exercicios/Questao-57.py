ListaSexoMasculino = ['M', 'm', 'Masculino', 'masculino', 'Homem', 'homem']
somaSalariosMasculinos = 0

ListaSexoFeminino = ['F', 'f', 'Feminino', 'feminino', 'Mulher', 'mulher']
somaSalariosFeminino = 0

ListaPararPrograma = ['N', 'n', 'Não', 'não', 'Nao', 'nao', 'NÃO', 'NAO', 'Parar', 'parar', 'PARAR']

while True:
    salario = float(input('Digite o salário do funcionário: '))
    sexo = input('Digite o sexo do funcionário: ')

    if sexo in ListaSexoMasculino:
        somaSalariosMasculinos += salario

    elif sexo in ListaSexoFeminino:
        somaSalariosFeminino += salario

    pararPrograma = input('Deseja continuar o programa?')
    print('-------------------------')

    if pararPrograma in ListaPararPrograma:
        print('O total pago aos homens foi de: R$%.2f' % somaSalariosMasculinos)
        print('O total pago as mulheres foi de: R$%.2f' % somaSalariosFeminino)
        break