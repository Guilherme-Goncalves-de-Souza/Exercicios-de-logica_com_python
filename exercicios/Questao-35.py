tipoCarro = input('Digite o tipo de carro alugado (popular ou luxo):')
diasAlugados = int(input('Digite por quantos dias foram alugados:'))
kmPercorridos = float(input('Digite quantos Km foram percorridos:'))

if(tipoCarro == 'popular' or tipoCarro == 'Popular'):
    precoDias = diasAlugados * 90
    if(kmPercorridos <= 100):
        precoKm = kmPercorridos * 0.20
    else:
        precoKm = kmPercorridos * 0.10
    precoTotal = precoDias + precoKm
    print('O total foi de %.2f' % precoTotal)

elif(tipoCarro == 'luxo' or tipoCarro == 'Luxo'):
    precoDias = diasAlugados * 150
    if(kmPercorridos <= 200):
        precoKm = kmPercorridos * 0.30
    else:
        precoKm = kmPercorridos * 0.25
    precoTotal = precoDias + precoKm
    print('O total foi de R$%.2f' % precoTotal)
else:
    print('Tipo de carro alugado NÃO encontrado!')