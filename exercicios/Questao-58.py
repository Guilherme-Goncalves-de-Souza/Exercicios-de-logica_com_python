listaIdadesAlunos = []

while(True):
    aluno = int(input('Digite a idade do aluno => '))
    print('--------')
    if (aluno == 999):
        break
    else:
        listaIdadesAlunos.append(aluno)


print(f'Existem {len(listaIdadesAlunos)} alunos na turma!')

mediaIdadeAlunos = sum(listaIdadesAlunos) / len(listaIdadesAlunos)
print('A média de idade do grupo é de: %.0f anos!' % mediaIdadeAlunos)