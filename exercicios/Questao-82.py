listaNotas = []
listaMediaMaiorTurma = []

for i in range(1, 11, 1):
    nota = float(input(f'Digite a {i}° nota: '))
    listaNotas.append(nota)

mediaTurma = (sum(listaNotas) / len(listaNotas))

print()
print(listaNotas)
for i in range(12):
    if i < len(listaNotas) and listaNotas[i] > mediaTurma:
        listaMediaMaiorTurma.append(i)

for i in range(1, 11, 1):
    print(f'{i:5}', end='')

print()
print('-----------------------')
print(f'A média de notas da turma foi de: {mediaTurma}.')
print(f'Há {len(listaMediaMaiorTurma)} alunos acima da média da turma.')
print(f'A maior nota da turma foi de {max(listaNotas)}.')

maiorNota = max(listaNotas)
for i in range(12):
    if i < len(listaNotas) and listaNotas[i] == maiorNota:
        print(f'A maior nota está na posição: {i+1}.')