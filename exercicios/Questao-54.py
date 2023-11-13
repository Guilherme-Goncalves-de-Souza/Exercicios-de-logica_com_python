listaPessoas = []
listaPesoMaiorNoventa = []
listaPeso_Altura_Menos = []
listaPeso_Altura_Mais = []

for i in range(1, 8, 1):
    peso = float(input(f'Digite o PESO da {i}° pessoa: '))
    altura = float(input(f'Digite a ALTURA da {i}° pessoa: '))
    print('-------------------------')
    if(peso >= 90):
        listaPesoMaiorNoventa.append(peso)

    if(peso <= 50 and altura <= 1.60):
        listaPeso_Altura_Menos.append((peso, altura))

    if(peso >= 100 and altura >= 1.90):
        listaPeso_Altura_Mais.append((peso, altura))

    listaPessoas.append((peso, altura))

for pessoas in listaPessoas:
    alturaGrupo = [tupla[1] for tupla in listaPessoas]

mediaAlturaGrupo = (sum(alturaGrupo) / len(listaPessoas))

print('A média de ALTURA do grupo foi de: %.2fm' % mediaAlturaGrupo)
print(f'A quantidade de pessoas que pesam mais de 90Kg foram de: {len(listaPesoMaiorNoventa)}')
print(f'A quantidade de pessoas que pesam menos de 50Kg e tem menos de 1.60m: {len(listaPeso_Altura_Menos)}')
print(f'A quantidade de pessoas medem mais de 1.90m e pesam mais de 100Kg: {len(listaPeso_Altura_Mais)}')
