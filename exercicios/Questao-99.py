def Potencia(n1, n2):
    potencia = n1 ** n2
    return potencia

base = int(input('Digite a base da potência: '))
expoente = int(input('Digite o expoente da potência: '))
print(f'A potência de {base} sobre {expoente} é de: {Potencia(base, expoente)}!')