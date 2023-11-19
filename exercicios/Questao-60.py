objetoPessoas = {}

listaIdadePessoas = []
listaMulheresIdade = []
listaHomensIdade = []

listaVerificaSexo = ['Homem', 'homem', 'Mulher', 'mulher']

listaVerificarEncerramento = ['Não', 'não', 'Nao', 'nao', 'N', 'n']


## FUNÇÕES:
def nome_pessoa_mais_velha(listaIdade, objeto):
    nome_pessoa = None

    idade_mais_velha_pessoas = max(listaIdade)
    for nome, chave in objeto.items():
        if chave['idade'] == idade_mais_velha_pessoas:
            nome_pessoa = nome
            break

    print(f'A pessoa mais velha é {nome_pessoa}, com {idade_mais_velha_pessoas} anos de idade.')

def nome_mulher_mais_jovem(listaIdade, objeto):
    nome_mulher = None

    idade_mais_nova_mulheres = min(listaIdade)
    for nome, chave in objeto.items():
        if chave['idade'] == idade_mais_nova_mulheres:
            nome_mulher = nome
            break

    print(f'A {nome_mulher} é a mulher mais jovem, com {idade_mais_nova_mulheres} anos.')

def homens_mais_30_anos():
    homens_mais_30 = 0

    for idade in listaHomensIdade:
        if(idade >= 30):
            homens_mais_30 += 1
    print(f'Há {homens_mais_30} homens que tem MAIS de 30 anos.')


def mulheres_menos_18_anos():
    mulheres_menos_18 = 0

    for idade in listaMulheresIdade:
        if(idade <= 18):
            mulheres_menos_18 += 1
    print(f'Há {mulheres_menos_18} mulheres com MENOS de 18 anos.')

## FIM FUNÇÕES


while True:
    print('------------')
    sexo = input('Digite o sexo da pessoa(homem ou mulher): ')

    if sexo in listaVerificaSexo:
        nome = input('Digite o nome da pessoa: ')
        idade = int(input('Digite a idade da pessoa: '))

        objetoPessoas[nome] = {'idade': idade, 'sexo': sexo}
        if sexo in listaVerificaSexo[0:2]:  # Homem:
            listaIdadePessoas.append(idade)
            listaHomensIdade.append(idade)

        elif sexo in listaVerificaSexo[2:4]: # Mulher:
            listaIdadePessoas.append(idade)
            listaMulheresIdade.append(idade)

        continuar = input('Deseja continuar? (S ou N)')
        if continuar in listaVerificarEncerramento:

            nome_pessoa_mais_velha(listaIdadePessoas, objetoPessoas)
            nome_mulher_mais_jovem(listaMulheresIdade, objetoPessoas)
            print('A média de idade é de %.0f anos.' % (sum(listaIdadePessoas) / len(listaIdadePessoas)))
            homens_mais_30_anos()
            mulheres_menos_18_anos()
            break

    else:
        print('##### ERROR :(')
        print('--Digite um sexo válido--')
        print('##### TENTE NOVAMENTE:')
        continue