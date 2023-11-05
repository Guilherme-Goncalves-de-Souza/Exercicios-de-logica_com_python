import random

print('!SORTEIO 20 NÚMEROS!')

listaNumerosSorteados = []
listaNumerosMaior5 = []
listaNumerosDiv3 = []

for i in range(1, 21, 1):
    numero = random.randint(0, 10)

    listaNumerosSorteados.append(numero)

    if(numero > 5):
        listaNumerosMaior5.append(numero)

    if(numero % 3 == 0):
        listaNumerosDiv3.append(numero)

print(f'Os números sorteados foram: {len(listaNumerosSorteados)}, sendo eles: {listaNumerosSorteados}')
print(f'Números acima de 5: {len(listaNumerosMaior5)}, sendo eles: {listaNumerosMaior5}')
print(f'Números divisíveis por 3: {len(listaNumerosDiv3)}, sendo eles: {listaNumerosDiv3}')
