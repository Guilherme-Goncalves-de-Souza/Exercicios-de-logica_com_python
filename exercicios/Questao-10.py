largura = float(input("Digite a largura da parede: "))
altura = (float(input("Digite a altura da parede: ")))

area = largura * altura

print(f"A área a ser pintada será de %.2f." % area)
print(f"A quantidade de tinta que deverá ser usada será de %.2f litros." % (area / 2))