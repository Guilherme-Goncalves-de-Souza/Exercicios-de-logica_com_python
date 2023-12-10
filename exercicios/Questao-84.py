listaGeral = []
listaIdades = []
listaMenoresIdade = []

for i in range(9):
    nome = input(f'Digite o nome da {i+1}° pessoa: ')
    idade = int(input(f'Digite a idade da {i+1}° pessoa: '))
    listaGeral.append((nome, idade))

    if(idade <= 18):
        listaMenoresIdade.append((nome, idade))
    else:
        listaIdades.append((nome, idade))

print(f'Lista com todas as pessoas: {listaGeral}')
print()
print(f'Lista das pessoas menores de idade: {listaMenoresIdade}')