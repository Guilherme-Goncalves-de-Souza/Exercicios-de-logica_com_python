listaNomes = []

for i in range(8):
    nome = input('Digite o nome: ')
    listaNomes.append(nome)
print(list(reversed(listaNomes)), end='')

print()

for i in range(8):
    print(f'{i:10}', end='')