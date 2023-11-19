listaMulheres = []
listaMulheresIdade = []
listaHomens = []
listaHomensIdade = []
listaIdadePessoas = []

listaVerificaSexoHomem = ['h', 'H', 'homem', 'Homem']
listaVerificaSexoMulher = ['m', 'M', 'mulher', 'Mulher']

listaVerificaEncerramento = ['n', 'N', 'nao', 'Nao', 'não', 'Não', 'parar', 'Parar', 'PARAR']

while True:
    sexo = input('Digite o sexo da pessoa(homem ou mulher) > ')

    if(sexo in listaVerificaSexoMulher or sexo in listaVerificaSexoHomem):
        idade = int(input('Digite a idade da pessoa > '))

        if sexo in listaVerificaSexoMulher:
            listaMulheres.append((sexo, idade))
            listaMulheresIdade.append(idade)
            listaIdadePessoas.append(idade)
        elif sexo in listaVerificaSexoHomem:
            listaHomens.append((sexo, idade))
            listaHomensIdade.append(idade)
            listaIdadePessoas.append(idade)
    else:
        print('###### ERROR :(')
        print('Digite um sexo válido(homem ou mulher)!')
        print('###### TENTE NOVAMENTE: ')
        continue

    print('---------------')
    parar = input('Deseja continuar o programa? ')
    print('---------------')

    if parar in listaVerificaEncerramento:
        print(f'A maior idade lida foi de {max(listaIdadePessoas)} anos.')
        print(f'A quantidade de homens cadastrados foi de {len(listaHomens)}.')
        print(f'A idade da mulher mais jovem é de: {min(listaMulheresIdade)} anos.')
        print('A média de idade dos homens é de: %.0f anos.' % (sum(listaHomensIdade) / len(listaHomensIdade)))
        break