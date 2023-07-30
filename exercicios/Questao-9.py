print("Quandos dólares posso comprar?")
print(" US$1,00 = R$3,45 ")

reais = float(input("Digite a quantidade de Reais que tem em sua carteira: "))

print(f"Com R${reais} reais, você pode comprar U$%.2f dólares" % (reais / 3.45))