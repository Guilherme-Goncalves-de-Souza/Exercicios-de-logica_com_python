listaIdade = []

listaVerificaEncerramento = ['Sim', 'sim', 'SIM', 'parar', 'Parar', 'PARAR', 's', 'S']

def pessoas_mais_21anos ():
    pessoasMais21 = 0
    for idade in listaIdade:
        if(idade >= 21):
            pessoasMais21 += 1

    print(f'Há {pessoasMais21} pessoas com mais de 21 anos.')

while True:
    idade = int(input('Digite a idade: '))
    listaIdade.append(idade)

    parar = input('Deseja parar(S ou N)? ')

    if parar in listaVerificaEncerramento:
        print(f'Foram digitadas {len(listaIdade)} idades.')
        print('A média de idades é de: %.0f anos.' % (sum(listaIdade) / len(listaIdade)))
        pessoas_mais_21anos()
        break