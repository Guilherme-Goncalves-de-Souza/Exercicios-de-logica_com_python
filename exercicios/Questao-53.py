homens = []
idadesHomens = []
mulheres = []
idadesMulheres = []
pessoas = []
idadesPessoas = []

sexoMasculino = ['M', 'm', 'Masculino', 'masculino']
sexoFeminino = ['F', 'f', 'Feminino', 'feminino']

for i in range(1, 6, 1):
    idade = int(input(f'Digite a idade da {i}° pessoa:'))
    sexo = input(f'Digite o sexo da {i}° pessoa:')
    print('---------------------------')
    if sexo in sexoMasculino:
        sexoLetra = 'M'
        homens.append((idade, sexoLetra))
        idadesHomens.append(idade)
    elif sexo in sexoFeminino:
        sexoLetra = 'F'
        mulheres.append((idade, sexoLetra))
        idadesMulheres.append(idade)
    pessoas.append((idade, sexoLetra))
    idadesPessoas.append(idade)

print(f'A quantidade de homens cadastrados foram de: {len(homens)}!')
print(f'A quantidade de mulheres cadastradas foram de: {len(mulheres)}!')
print(f'A média de idade do grupo foi de: {(sum(idadesPessoas) / 5)}!')
print(f'A média de idade dos homens foi de: {(sum(idadesHomens) / len(idadesHomens))}!')

idadeMaisVinte = 0
for i in idadesMulheres:
    if i > 20:
        idadeMaisVinte += 1

print(f'A quantidade de mulheres com mais de 20 anos: {idadeMaisVinte}!')
