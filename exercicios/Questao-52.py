listaPessoas = []
listaPessoasMais18 = []
listaPessoasMenos5 = []

for i in range(1, 11, 1):
    idades = int(input(f'Digite a idade da pessoa {i}: '))
    listaPessoas.append(idades)

    if(idades >= 18):
        listaPessoasMais18.append(idades)
    elif(idades <= 5):
        listaPessoasMenos5.append(idades)

print(f'-> A média de idade foi de {sum(listaPessoas) / 10} anos.')
print(f'-> Há {len(listaPessoasMais18)} pessoas com mais de 18 anos.')
print(f'-> Há {len(listaPessoasMenos5)} crianças com menos de 5 anos.')
print(f'-> A maior idade foi de {max(listaPessoas)} anos.')
