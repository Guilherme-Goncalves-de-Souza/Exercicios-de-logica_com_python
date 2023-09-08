distancia = float(input("Digite a distância em KM que você deseja percorrer: "))

if (distancia <= 200):
    preco_passagem = distancia * 0.50
    print(f"Com a distância de {distancia}, você pagará R$ %.2f." % preco_passagem)
else:
    preco_passagem = distancia * 0.45
    print(f"Com a distância de {distancia}, você pagará R$ %.2f." % preco_passagem)
