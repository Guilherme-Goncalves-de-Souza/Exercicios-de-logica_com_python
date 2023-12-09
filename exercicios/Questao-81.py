listaIdades = []
listaPosicaoIdadeMais25 = []

for i in range(1, 9, 1):
    idade = int(input(f'Digite a {i}° idade: '))
    listaIdades.append(idade)

    if(idade >= 25):
        listaPosicaoIdadeMais25.append(i)

print(listaIdades)
for i in range(1, 9, 1):
    print(f'{i:3}', end='')

print()
print(f'A média de idade das pessoas foi de: {(sum(listaIdades) / len(listaIdades)):.0f} anos.')
print(f'Nas posições: {listaPosicaoIdadeMais25} temos as pessoas com idade maior que 25 anos.')
print(f'A maior idade foi a de: {max(listaIdades)} anos.')

maiorIdade = max(listaIdades)
for i in range(1, 9, 1):
     if i < len(listaIdades) and listaIdades[i] == maiorIdade:
         posicaoIdade = i

print(f'Na posição {posicaoIdade} temos a maior idade!')