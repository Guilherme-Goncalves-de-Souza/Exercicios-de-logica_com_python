listaGeralFuncionarios = []
listaFuncionariasMais5mil = []

listaVerificaSexoHomem = ['h', 'H', 'homem', 'Homem', 'Masculino', 'masculino']
listaVerificaSexoMulher = ['m', 'M', 'Mulher', 'mulher', 'Feminino', 'feminino']

i = 0
while True:
    if(i == 5):
        break

    else:
        sexo = input(f'Digite o sexo do(a) {i+1}° funcionário(a), (H ou M): ')

        if(sexo in listaVerificaSexoHomem or sexo in listaVerificaSexoMulher):
            nome = input(f'Digite o nome do(a) {i + 1}° funcionário(a): ')
            salario = float(input(f'Digite o salário do(a) {i + 1}° funcionário(a): '))

            if(sexo in listaVerificaSexoMulher):
                if(salario >= 5000):
                    listaFuncionariasMais5mil.append((nome, sexo, salario))
            i+= 1
        else:
            print('Digite um sexo válido, (H ou M)!')
            continue

print('--------------')
print(f'Existem {len(listaFuncionariasMais5mil)} mulheres que ganham mais de R$5 mil!')
if(len(listaFuncionariasMais5mil) != 0):
    print(f'São elas: {listaFuncionariasMais5mil}')

