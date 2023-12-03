listaPesoHomens = []
listaPesoMulheres = []
listaHomemMais100Kg = []

listaVerificaHomem = ['Homem', 'homem', 'HOMEM', 'H', 'h']
listaVerificaMulher = ['Mulher', 'mulher', 'MULHER', 'M', 'm']

i = 0

while i < 8:
    sexo = input('Digite o sexo: ')

    if sexo in listaVerificaHomem or sexo in listaVerificaMulher:
        peso = float(input('Digite o peso: '))

        if sexo in listaVerificaHomem:
            listaPesoHomens.append(peso)
            if(peso >= 100):
                listaHomemMais100Kg.append(peso)

        elif sexo in listaVerificaMulher:
            listaPesoMulheres.append(peso)

        print('--------')

    else:
        print('Digite um sexo válido!')
        print('---------------')
        continue

    i += 1

def mediaPesoMulheres(listaMulheres):
    if len(listaMulheres) == 0:
        print('Não há mulheres cadastradas para fazer a média de peso!')
    else:
        print(f'A média de peso das mulheres é de: {(sum(listaPesoMulheres) / len(listaPesoMulheres)):.2f} KG!')


print(f'A quantidade de mulheres cadastradas foi de: {len(listaPesoMulheres)}!')
print(f'Há {len(listaHomemMais100Kg)} homens com mais de 100 KG!')
mediaPesoMulheres(listaPesoMulheres)
print(f'O maior peso entre os homens é de: {max(listaPesoHomens): .2f} KG!')
