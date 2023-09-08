nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (Homem ou Mulher): ")
valor_compras = float(input("Digite o valor da compra em R$: "))

if (sexo == "Homem" or sexo == "H"):
    desconto = valor_compras * 0.05
    valor_total = valor_compras - desconto
    print(f"{nome}, o valor do desconto foi de: %.2f " % desconto)
    print("Sendo assim o valor final é de: R$ %.2f" % valor_total)

elif (sexo == "Mulher" or sexo == "M"):
    desconto = valor_compras * 0.13
    valor_total = valor_compras - desconto
    print(f"{nome}, o valor do desconto foi de: %.2f " % desconto)
    print("Sendo assim o valor final é de: R$ %.2f" % valor_total)

else:
    print("Digite um sexo válido. EX: Homem ou Mulher")