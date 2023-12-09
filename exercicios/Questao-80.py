from random import randint
listaNumerosVetores = []

numeroUsuario = int(input('Digite um número: '))
listaPosicoesNumeroEscolhido = []

for i in range(30):
    numero = randint(0,15)
    listaNumerosVetores.append(numero)

    if(numero == numeroUsuario):
        listaPosicoesNumeroEscolhido.append(i)

print()
print(listaNumerosVetores)
for i in range(30):
    print(f'{i:4}', end='')

print()
print('---------------------')
print(f'NÚMERO ESCOLHIDO: {numeroUsuario}.')
print(f'Esse número foi sorteado {len(listaPosicoesNumeroEscolhido)} vezes.')
print(f'O número sorteado está nas posições: {listaPosicoesNumeroEscolhido}')
