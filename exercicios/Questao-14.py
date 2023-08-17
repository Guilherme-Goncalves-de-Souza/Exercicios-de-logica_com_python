km_percorridos = float(input("Digite a quantidade de KM percorrido pelo carro: "))
dias = int(input("Digite a quantidade de DIAS que o carro foi alugado: "))

preco_total = (km_percorridos * 0.20) + (dias * 90)

print("O valor total a ser pago será de R$ %.2f" % preco_total)