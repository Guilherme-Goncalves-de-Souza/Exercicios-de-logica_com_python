preco = int(input("Digite o preço de um produto: "))
valor_desconto = int(input("Digite a % do desconto: "))

desconto = preco * (valor_desconto / 100)
preco_promocional = preco - desconto

print(f"Com o desconto de {valor_desconto}%, o preço final ficou em:")
print("R$ %.2f" % preco_promocional)
