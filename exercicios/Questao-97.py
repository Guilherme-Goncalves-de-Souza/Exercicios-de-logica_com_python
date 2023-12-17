def Maior(lista):
    maiorNumero = max(lista)
    return maiorNumero

listaNumbers = []

for i in range(3):
    number = int(input(f'Digite o {i+1}° número: '))
    listaNumbers.append(number)

print(f'O maior número entre: {listaNumbers} é o {Maior(listaNumbers)}!')